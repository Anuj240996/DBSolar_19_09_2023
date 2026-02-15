from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Lead, Stage, LeadActivity, SiteSurvey, Opportunity
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.conf import settings
from .forms import LeadForm
from django.contrib import messages
from django.utils import timezone
import logging
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
import csv
from io import StringIO
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.utils.text import slugify
import os
from django.conf import settings
import uuid
from django.contrib.auth import get_user_model
from django.urls import reverse

logger = logging.getLogger(__name__)


@login_required
def leads_list(request):
    # Build base queryset
    stages = Stage.objects.order_by('order')
    qs = Lead.objects.select_related('assigned_to', 'stage')

    # Filters
    q = request.GET.get('q', '').strip()
    date_from = request.GET.get('from', '')
    date_to = request.GET.get('to', '')
    stage_id = request.GET.get('stage', '')
    assigned = request.GET.get('assigned', '')
    source = request.GET.get('source', '')
    score = request.GET.get('score', '')
    city = request.GET.get('city', '')

    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(phone__icontains=q) | Q(address__icontains=q))
    if date_from:
        try:
            qs = qs.filter(created_at__date__gte=date_from)
        except Exception:
            pass
    if date_to:
        try:
            qs = qs.filter(created_at__date__lte=date_to)
        except Exception:
            pass
    if stage_id:
        try:
            qs = qs.filter(stage__id=int(stage_id))
        except Exception:
            qs = qs.filter(status=stage_id)
    if assigned:
        try:
            qs = qs.filter(assigned_to__id=int(assigned))
        except Exception:
            pass
    if source:
        qs = qs.filter(source__icontains=source)
    if score:
        qs = qs.filter(score=score)
    if city:
        qs = qs.filter(city__icontains=city)

    qs = qs.order_by('-created_at')

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(qs, 25)
    try:
        leads_page = paginator.page(page)
    except PageNotAnInteger:
        leads_page = paginator.page(1)
    except EmptyPage:
        leads_page = paginator.page(paginator.num_pages)

    logger.info("leads_list: returning %s leads (filtered) for user=%s", qs.count(), request.user)
    context = {
        'stages': stages,
        'leads': leads_page,
        'paginator': paginator,
        'query': q,
        'filters': {
            'from': date_from,
            'to': date_to,
            'stage': stage_id,
            'assigned': assigned,
            'source': source,
            'score': score,
            'city': city,
        }
    }
    return render(request, 'leads/leads_list.html', context)


@login_required
def leads_export(request):
    # export filtered leads as CSV (uses same filters as leads_list)
    qs = Lead.objects.select_related('assigned_to', 'stage').all().order_by('-created_at')
    q = request.GET.get('q', '').strip()
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(phone__icontains=q) | Q(address__icontains=q))
    # (reuse other filters as needed)
    # prepare CSV
    buf = StringIO()
    writer = csv.writer(buf)
    writer.writerow(['id', 'name', 'phone', 'city', 'source', 'campaign', 'score', 'status', 'stage', 'assigned_to', 'created_at'])
    for l in qs:
        writer.writerow([l.id, l.name, l.phone, l.city, l.source, l.campaign, l.score, l.status, (l.stage.name if l.stage else ''), (l.assigned_to.username if l.assigned_to else ''), l.created_at.isoformat()])
    resp = HttpResponse(buf.getvalue(), content_type='text/csv')
    resp['Content-Disposition'] = 'attachment; filename=leads_export.csv'
    return resp


@login_required
def leads_api_list(request):
    """Simple JSON endpoint to return leads for debugging."""
    qs = Lead.objects.all().order_by('-created_at')[:200]
    data = []
    for l in qs:
        data.append({
            'id': l.id,
            'name': l.name,
            'phone': l.phone,
            'city': l.city,
            'status': l.status,
            'created_at': l.created_at.isoformat(),
        })
    return JsonResponse({'count': qs.count(), 'leads': data})


@login_required
def lead_create(request):
    logger.info("lead_create called: user=%s method=%s", request.user, request.method)
    if request.method == "POST":
        logger.info("lead_create: POST data keys=%s", list(request.POST.keys()))
        form = LeadForm(request.POST)
        logger.info("lead_create: form instantiated")
        if form.is_valid():
            logger.info("lead_create: form is valid")
            lead = form.save(commit=False)
            # set created_by and ensure customer_id left blank (auto background)
            lead.created_by = request.user
            lead.customer_id = lead.customer_id or None
            lead.save()
            # create initial activity
            try:
                LeadActivity.objects.create(lead=lead, user=request.user, type='note', note='Lead created')
            except Exception:
                pass
            messages.success(request, "Lead created successfully.")
            return redirect('leads:lead_detail', pk=lead.pk)
    else:
        form = LeadForm()
        logger.info("lead_create: rendered empty form for GET")
    return render(request, 'leads/lead_create.html', {'form': form})


@login_required
def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    activities = lead.activities.all()
    stages = Stage.objects.order_by('order')
    # provide list of engineers for scheduling UI
    User = get_user_model()
    engineers = User.objects.filter(is_staff=True)[:50]
    context = {'lead': lead, 'activities': activities, 'stages': stages, 'engineers': engineers}
    return render(request, 'leads/lead_detail.html', context)


@login_required
def pipeline_view(request):
    stages = Stage.objects.order_by('order')
    stage_groups = []
    for s in stages:
        stage_groups.append((s, Lead.objects.filter(stage=s).select_related('assigned_to')[:200]))
    context = {'stage_groups': stage_groups, 'stages': stages}
    return render(request, 'leads/pipeline.html', context)


@require_POST
@login_required
def update_lead_stage(request, pk):
    try:
        new_stage = request.POST.get('stage')
    except Exception:
        return HttpResponseBadRequest("Invalid stage")
    lead = get_object_or_404(Lead, pk=pk)
    old = lead.status
    # new_stage may be id (from _lead_card); try resolve
    try:
        # if sent as id
        stage_obj = Stage.objects.get(pk=int(new_stage))
        new_stage_name = stage_obj.name
    except Exception:
        new_stage_name = new_stage
        stage_obj = None
    lead.status = new_stage_name
    if stage_obj:
        # keep stage FK if model has it
        try:
            lead.stage = stage_obj
        except Exception:
            pass
    lead.save()
    LeadActivity.objects.create(lead=lead, type='stage', note=f"Moved from {old} to {new_stage_name}", user=request.user)

    # If HTMX request, return updated card HTML fragment so UI updates in place
    if request.headers.get('Hx-Request') == 'true' or request.META.get('HTTP_HX_REQUEST') == 'true':
        html = render_to_string('leads/_lead_card.html', {'lead': lead, 'stages': Stage.objects.order_by('order')}, request=request)
        return HttpResponse(html)

    return JsonResponse({'status': 'ok', 'new_stage': new_stage_name})


@require_POST
@login_required
def add_activity(request, pk):
    """Add an activity (note/call) to a lead."""
    lead = get_object_or_404(Lead, pk=pk)
    atype = request.POST.get('type', 'note')
    note = request.POST.get('note', '')
    # optional follow-up datetime
    next_fu = request.POST.get('next_follow_up') or request.POST.get('next_followup') or None
    if next_fu:
        try:
            from django.utils.dateparse import parse_datetime
            ndt = parse_datetime(next_fu)
            if ndt:
                lead.next_follow_up = ndt
                lead.save()
        except Exception:
            pass
    activity = LeadActivity.objects.create(lead=lead, user=request.user, type=atype, note=note)
    # If HTMX request, return updated activities fragment
    if request.headers.get('Hx-Request') == 'true' or request.META.get('HTTP_HX_REQUEST') == 'true':
        activities = lead.activities.all()
        html = render_to_string('leads/_activities.html', {'activities': activities}, request=request)
        return HttpResponse(html)
    return redirect('leads:lead_detail', pk=lead.pk)


@login_required
def activities_fragment(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    activities = lead.activities.all()
    html = render_to_string('leads/_activities.html', {'activities': activities}, request=request)
    return HttpResponse(html)


@login_required
def lead_edit(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            LeadActivity.objects.create(lead=lead, user=request.user, type='note', note='Lead updated')
            messages.success(request, "Lead updated.")
            return redirect('leads:lead_detail', pk=lead.pk)
    else:
        form = LeadForm(instance=lead)
    return render(request, 'leads/lead_create.html', {'form': form, 'lead': lead})


@require_POST
@login_required
def mark_lost(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    reason = request.POST.get('reason', '')
    old = lead.status
    lead.status = 'lost'
    # try to attach a lost stage if configured
    try:
        lost_stage = Stage.objects.filter(is_lost=True).first()
        if lost_stage:
            lead.stage = lost_stage
    except Exception:
        pass
    lead.save()
    LeadActivity.objects.create(lead=lead, user=request.user, type='note', note=f"Marked lost. Reason: {reason}")
    if request.headers.get('Hx-Request') == 'true' or request.META.get('HTTP_HX_REQUEST') == 'true':
        # return updated lead card for pipeline
        html = render_to_string('leads/_lead_card.html', {'lead': lead, 'stages': Stage.objects.order_by('order')}, request=request)
        return HttpResponse(html)
    return redirect('leads:lead_detail', pk=lead.pk)


@require_POST
@login_required
def convert_to_opportunity(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    opp = Opportunity.objects.create(
        lead=lead,
        total_system_cost=request.POST.get('total_system_cost') or lead.opportunity_value or None,
        probability=request.POST.get('probability') or lead.probability or 0,
        expected_close=request.POST.get('expected_close') or lead.expected_close or None,
    )
    LeadActivity.objects.create(lead=lead, user=request.user, type='conversion', note=f"Converted to opportunity #{opp.pk}")
    # link on lead
    lead.convert_customer_id = lead.customer_id or lead.convert_customer_id
    lead.save()
    if request.headers.get('Hx-Request') == 'true' or request.META.get('HTTP_HX_REQUEST') == 'true':
        return JsonResponse({'ok': True, 'opportunity_id': opp.pk})
    return redirect('leads:lead_detail', pk=lead.pk)


@login_required
def dashboard(request):
    total_leads = Lead.objects.count()
    # Use Django timezone to compute today's date safely
    try:
        today = timezone.now().date()
        new_leads_today = Lead.objects.filter(created_at__date=today).count()
    except Exception:
        new_leads_today = Lead.objects.count()
    return render(request, 'leads/dashboard.html', {'total_leads': total_leads, 'new_leads_today': new_leads_today})


@login_required
def surveys_list(request):
    surveys = SiteSurvey.objects.select_related('assigned_engineer', 'lead').all().order_by('-created_at')[:200]
    return render(request, 'leads/surveys_list.html', {'surveys': surveys})


@login_required
def create_survey(request):
    """Create a SiteSurvey for a lead. HTMX-friendly."""
    if request.method == 'POST':
        lead_id = request.POST.get('lead_id')
        assigned_engineer = request.POST.get('assigned_engineer') or None
        scheduled_at = request.POST.get('scheduled_at') or None
        recommended_size = request.POST.get('recommended_size_kw') or None
        lead = get_object_or_404(Lead, pk=lead_id)
        survey = SiteSurvey.objects.create(
            lead=lead,
            assigned_engineer_id=(int(assigned_engineer) if assigned_engineer else None),
            scheduled_at=scheduled_at or None,
            recommended_size_kw=(recommended_size or None),
        )
        LeadActivity.objects.create(lead=lead, user=request.user, type='visit', note=f"Survey scheduled (id={survey.pk})")
        html = render_to_string('leads/_survey_card.html', {'survey': survey}, request=request)
        return HttpResponse(html)
    return HttpResponseBadRequest("Invalid method")


@login_required
def survey_detail(request, pk):
    survey = get_object_or_404(SiteSurvey, pk=pk)
    return render(request, 'leads/survey_detail.html', {'survey': survey})


@require_POST
@login_required
def survey_upload_image(request, pk):
    survey = get_object_or_404(SiteSurvey, pk=pk)
    files = request.FILES.getlist('images')
    saved = []
    for f in files:
        # safe filename
        ext = os.path.splitext(f.name)[1]
        name = slugify(os.path.splitext(f.name)[0])[:50]
        filename = f"surveys/{survey.id}/{name}-{uuid.uuid4().hex}{ext}"
        path = default_storage.save(filename, f)
        url = (settings.MEDIA_URL.rstrip('/') + '/' + path).replace('//', '/')
        saved.append(url)
    if saved:
        survey.images = (survey.images or []) + saved
        survey.save()
        LeadActivity.objects.create(lead=survey.lead, user=request.user, type='visit', note=f"Uploaded {len(saved)} survey images")
    # return updated survey card fragment
    html = render_to_string('leads/_survey_card.html', {'survey': survey}, request=request)
    return HttpResponse(html)


@require_POST
@login_required
def approve_for_quotation(request, pk):
    survey = get_object_or_404(SiteSurvey, pk=pk)
    # mark feasible if provided
    feasibility = request.POST.get('feasibility')
    if feasibility is not None:
        survey.feasibility = (feasibility.lower() in ('1', 'true', 'yes', 'on'))
    # optional recommended size override
    rec = request.POST.get('recommended_size_kw')
    if rec:
        try:
            survey.recommended_size_kw = float(rec)
        except Exception:
            pass
    survey.save()
    # create an Opportunity as placeholder for quotation flow
    opp = Opportunity.objects.create(
        lead=survey.lead,
        total_system_cost=request.POST.get('total_system_cost') or None,
        probability=request.POST.get('probability') or 60,
        expected_close=request.POST.get('expected_close') or None,
        status='quotation'
    )
    survey.lead.status = 'quote_sent'
    survey.lead.save()
    LeadActivity.objects.create(lead=survey.lead, user=request.user, type='quotation', note=f"Survey approved for quotation (survey={survey.pk}, opp={opp.pk})")
    # Try to create a Quotation in the quotation app and redirect to its edit page.
    try:
        from quotation.models import Quotation, PlantCapacity
        # Determine plant capacity: prefer recommended_size_kw, else fallback to 3.30
        cap_val = survey.recommended_size_kw or survey.lead.extra.get('recommended_size_kw') if isinstance(survey.lead.extra, dict) else None
        if cap_val:
            # try find exact or nearest PlantCapacity
            pc = PlantCapacity.objects.filter(capacity=cap_val).first()
            if not pc:
                # create a new PlantCapacity record
                pc = PlantCapacity.objects.create(capacity=cap_val)
        else:
            pc = PlantCapacity.objects.order_by('capacity').first()
        # Build minimal quotation
        q = Quotation.objects.create(
            consumer_name=survey.lead.name or 'Unknown',
            consumer_mobile=survey.lead.phone or '',
            consumer_address1=(survey.lead.address or '')[:255],
            consumer_state=survey.lead.state or '',
            consumer_email=survey.lead.email or '',
            plant_capacity_kw=pc or (PlantCapacity.objects.first() if PlantCapacity.objects.exists() else None),
            project_type='RoofTop',
            consumer_type='Residential',
        )
        LeadActivity.objects.create(lead=survey.lead, user=request.user, type='quotation', note=f"Quotation created #{q.pk} from survey {survey.pk}")
        # Link quotation id on opportunity/lead for traceability
        try:
            opp.quotation_id = q.pk
            opp.save()
        except Exception:
            pass
        survey.lead.quotation_id = q.pk
        survey.lead.save()
        # If HTMX call, return updated survey card; otherwise redirect to quotation edit page
        if request.headers.get('Hx-Request') == 'true' or request.META.get('HTTP_HX_REQUEST') == 'true':
            html = render_to_string('leads/_survey_card.html', {'survey': survey}, request=request)
            return HttpResponse(html)
        try:
            return redirect(reverse('quotation:edit_quotation', args=[q.pk]))
        except Exception:
            return redirect('leads:survey_detail', pk=survey.pk)
    except Exception:
        # fallback: return updated survey card fragment
        html = render_to_string('leads/_survey_card.html', {'survey': survey}, request=request)
        return HttpResponse(html)


@login_required
def quotations_list(request):
    try:
        return redirect('quotation:quotation_list')
    except Exception:
        return render(request, 'leads/quotations.html', {})


@login_required
def revenue_view(request):
    return render(request, 'leads/revenue.html', {})


@login_required
def analytics_view(request):
    return render(request, 'leads/analytics.html', {})


@login_required
def sales_team_view(request):
    return render(request, 'leads/sales_team.html', {})


@login_required
def settings_view(request):
    # show counts and links, but avoid querying tables that might not exist yet
    from django.db import connection
    table_names = connection.introspection.table_names()
    counts = {'stages': 0, 'sources': 0, 'campaigns': 0, 'lost_reasons': 0, 'scoring_rules': 0}
    try:
        from .models import LeadSource, Campaign, LostReason, ScoringRule, Stage
        if 'leads_stage' in table_names:
            counts['stages'] = Stage.objects.count()
        if 'leads_leadsource' in table_names:
            counts['sources'] = LeadSource.objects.count()
        if 'leads_campaign' in table_names:
            counts['campaigns'] = Campaign.objects.count()
        if 'leads_lostreason' in table_names:
            counts['lost_reasons'] = LostReason.objects.count()
        if 'leads_scoringrule' in table_names:
            counts['scoring_rules'] = ScoringRule.objects.count()
    except Exception:
        # keep defaults (0) if models or DB not ready
        pass
    return render(request, 'leads/settings.html', {'counts': counts})

