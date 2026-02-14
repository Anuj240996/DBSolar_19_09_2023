from django.contrib import admin
from .models import Stage, Lead, Activity


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_won', 'is_lost')
    ordering = ('order',)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'location', 'score', 'stage', 'assigned_to', 'next_followup', 'created_date')
    list_filter = ('score', 'stage', 'assigned_to', 'source')
    search_fields = ('name', 'phone', 'location', 'customer__Comp_name')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('lead', 'type', 'created_by', 'created_at')
    list_filter = ('type', 'created_by')

