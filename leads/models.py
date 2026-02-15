from django.db import models
from django.conf import settings

USER = settings.AUTH_USER_MODEL


class Stage(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    is_won = models.BooleanField(default=False)
    is_lost = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Lead(models.Model):
    SCORE_CHOICES = (
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    )

    # Use integer reference to customer to avoid cross-app FK ordering problems
    customer_id = models.BigIntegerField(null=True, blank=True)
    # stage FK to track pipeline stage
    stage = models.ForeignKey('Stage', on_delete=models.SET_NULL, null=True, blank=True, related_name='leads')
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=120, blank=True)
    state = models.CharField(max_length=120, blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    property_type = models.CharField(max_length=30, blank=True)
    roof_type = models.CharField(max_length=120, blank=True)
    electricity_bill = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    budget_estimate = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    source = models.CharField(max_length=120, blank=True)
    campaign = models.CharField(max_length=255, blank=True)

    assigned_to = models.ForeignKey(USER, null=True, blank=True, on_delete=models.SET_NULL, related_name='leads')
    score = models.IntegerField(default=0)
    status = models.CharField(max_length=32, default='new')
    # follow-up scheduling
    next_follow_up = models.DateTimeField(null=True, blank=True)
    # opportunity / forecasting fields
    opportunity_value = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    probability = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    expected_close = models.DateField(null=True, blank=True)
    # Tags stored as JSON list for flexibility. Added to match existing DB which had a non-null tags column.
    tags = models.JSONField(default=list, blank=True)

    quotation_id = models.BigIntegerField(null=True, blank=True)
    convert_customer_id = models.BigIntegerField(null=True, blank=True)

    created_by = models.ForeignKey(USER, null=True, blank=True, on_delete=models.SET_NULL, related_name='leads_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    extra = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.phone or 'no-phone'}"


class LeadActivity(models.Model):
    ACTIVITY_TYPES = [
        ('call', 'Call'),
        ('whatsapp', 'WhatsApp'),
        ('email', 'Email'),
        ('note', 'Note'),
        ('visit', 'Site Visit'),
        ('quotation', 'Quotation'),
        ('conversion', 'Conversion'),
        ('stage', 'Stage Change'),
    ]
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='activities')
    user = models.ForeignKey(USER, null=True, blank=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=32, choices=ACTIVITY_TYPES)
    note = models.TextField(blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_type_display()} on {self.created_at:%Y-%m-%d} for {self.lead}"


class SiteSurvey(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='surveys')
    assigned_engineer = models.ForeignKey(USER, null=True, blank=True, on_delete=models.SET_NULL, related_name='surveys')
    scheduled_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    checklist = models.JSONField(default=dict, blank=True)
    images = models.JSONField(default=list, blank=True)
    feasibility = models.BooleanField(null=True, blank=True)
    recommended_size_kw = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Survey for {self.lead} ({self.scheduled_at or 'unscheduled'})"


class Opportunity(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='opportunities')
    quotation_id = models.BigIntegerField(null=True, blank=True)
    total_system_cost = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    subsidy = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    roi = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    emi = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    payback_period_months = models.IntegerField(null=True, blank=True)
    probability = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    expected_close = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, default='open')

    def __str__(self):
        return f"Opp for {self.lead} — {self.status}"


class RevenueRecord(models.Model):
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE, related_name='revenues', null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    recorded_date = models.DateField(auto_now_add=True)
    recorded_by = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.amount} on {self.recorded_date}"


class LeadSource(models.Model):
    name = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=200, unique=True)
    source = models.ForeignKey(LeadSource, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.name


class LostReason(models.Model):
    reason = models.CharField(max_length=255)
    def __str__(self):
        return self.reason


class ScoringRule(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    weight = models.IntegerField(default=1)
    active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.name} ({self.weight})"

