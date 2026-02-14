from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer


class Stage(models.Model):
    """
    Lead stages (New, Qualified, Survey, Quote, Negotiation, Won, Lost)
    """
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

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    electricity_bill = models.IntegerField(null=True, blank=True)
    property_type = models.CharField(max_length=100, blank=True, null=True)
    score = models.CharField(max_length=10, choices=SCORE_CHOICES, default='medium')
    source = models.CharField(max_length=100, blank=True, null=True)
    campaign = models.CharField(max_length=100, blank=True, null=True)
    stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True, related_name='leads')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_leads')
    next_followup = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    bill_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.name} ({self.phone})"


class Activity(models.Model):
    ACTIVITY_TYPES = (
        ('call', 'Call Logged'),
        ('whatsapp', 'WhatsApp Sent'),
        ('email', 'Email Sent'),
        ('note', 'Note Added'),
        ('followup', 'Follow-up Scheduled'),
        ('stage', 'Stage Changed'),
        ('quotation', 'Quotation Sent'),
    )
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    note = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_for = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_type_display()} - {self.lead}"

