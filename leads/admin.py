from django.contrib import admin
from .models import Stage, Lead, LeadActivity, SiteSurvey, Opportunity, RevenueRecord, LeadSource, Campaign, LostReason, ScoringRule


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_won', 'is_lost')


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'city', 'score', 'status', 'stage', 'assigned_to', 'created_at')
    list_filter = ('score', 'status', 'stage', 'assigned_to', 'source')
    search_fields = ('name', 'phone', 'address', 'campaign')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('name', 'phone', 'email', 'address', 'city', 'state')}),
        ('Property', {'fields': ('property_type', 'roof_type', 'electricity_bill', 'budget_estimate')}),
        ('Pipeline', {'fields': ('stage', 'status', 'assigned_to', 'next_follow_up', 'opportunity_value', 'probability', 'expected_close')}),
        ('Meta', {'fields': ('customer_id', 'quotation_id', 'created_by', 'created_at', 'updated_at')}),
    )


@admin.register(LeadActivity)
class LeadActivityAdmin(admin.ModelAdmin):
    list_display = ('lead', 'type', 'user', 'created_at')


@admin.register(SiteSurvey)
class SiteSurveyAdmin(admin.ModelAdmin):
    list_display = ('lead', 'assigned_engineer', 'scheduled_at', 'completed_at', 'feasibility')


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('lead', 'status', 'total_system_cost', 'probability', 'expected_close')


@admin.register(RevenueRecord)
class RevenueRecordAdmin(admin.ModelAdmin):
    list_display = ('opportunity', 'amount', 'recorded_date', 'recorded_by')


@admin.register(LeadSource)
class LeadSourceAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'source')


@admin.register(LostReason)
class LostReasonAdmin(admin.ModelAdmin):
    list_display = ('reason',)


@admin.register(ScoringRule)
class ScoringRuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'active')

