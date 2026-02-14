from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Lead, Stage, Activity
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.db.models import Q


@login_required
def leads_list(request):
    """Two-panel leads list with basic filters"""
    stages = Stage.objects.order_by('order')
    qs = Lead.objects.select_related('stage', 'assigned_to')
    # filters
    q = request.GET.get('q')
    stage = request.GET.get('stage')
    assigned = request.GET.get('assigned')
    score = request.GET.get('score')
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(phone__icontains=q) | Q(location__icontains=q))
    if stage:
        qs = qs.filter(stage__id=stage)
    if assigned:
        qs = qs.filter(assigned_to__id=assigned)
    if score:
        qs = qs.filter(score=score)

    leads = qs.order_by('-created_date')[:200]
    users = User.objects.filter(is_active=True).order_by('username')
    context = {'stages': stages, 'leads': leads, 'users': users}
    return render(request, 'customer/crm/leads_list.html', context)


@login_required
def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    activities = lead.activities.all()
    stages = Stage.objects.order_by('order')
    context = {'lead': lead, 'activities': activities, 'stages': stages}
    return render(request, 'customer/crm/lead_detail.html', context)


@login_required
def pipeline_view(request):
    stages = Stage.objects.order_by('order')
    stage_groups = []
    for s in stages:
        stage_groups.append((s, Lead.objects.filter(stage=s).select_related('assigned_to')[:200]))
    context = {'stage_groups': stage_groups, 'stages': stages}
    return render(request, 'customer/crm/pipeline.html', context)


@require_POST
@login_required
def update_lead_stage(request, pk):
    """API endpoint to move a lead to another stage"""
    try:
        new_stage_id = int(request.POST.get('stage_id'))
    except (TypeError, ValueError):
        return HttpResponseBadRequest("Invalid stage id")
    lead = get_object_or_404(Lead, pk=pk)
    new_stage = get_object_or_404(Stage, pk=new_stage_id)
    old_stage = lead.stage
    lead.stage = new_stage
    lead.save()
    Activity.objects.create(lead=lead, type='stage', note=f"Moved from {old_stage} to {new_stage}", created_by=request.user)
    return JsonResponse({'status': 'ok', 'new_stage': new_stage.name})

