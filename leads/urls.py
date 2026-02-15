from django.urls import path
from . import views

app_name = 'leads'

urlpatterns = [
    path('', views.leads_list, name='leads_list'),
    path('create/', views.lead_create, name='lead_create'),
    path('<int:pk>/', views.lead_detail, name='lead_detail'),
    path('pipeline/', views.pipeline_view, name='pipeline'),
    path('api/<int:pk>/stage/', views.update_lead_stage, name='update_lead_stage'),
    path('api/<int:pk>/activity/', views.add_activity, name='add_activity'),
    path('<int:pk>/activities_fragment/', views.activities_fragment, name='activities_fragment'),
    path('<int:pk>/edit/', views.lead_edit, name='lead_edit'),
    path('<int:pk>/mark_lost/', views.mark_lost, name='mark_lost'),
    path('<int:pk>/convert/', views.convert_to_opportunity, name='convert_to_opportunity'),
    path('api/list/', views.leads_api_list, name='leads_api_list'),
    path('export/', views.leads_export, name='leads_export'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('surveys/', views.surveys_list, name='surveys'),
    path('surveys/create/', views.create_survey, name='create_survey'),
    path('surveys/<int:pk>/', views.survey_detail, name='survey_detail'),
    path('surveys/<int:pk>/upload_image/', views.survey_upload_image, name='survey_upload_image'),
    path('surveys/<int:pk>/approve/', views.approve_for_quotation, name='survey_approve'),
    path('quotations/', views.quotations_list, name='quotations'),
    path('revenue/', views.revenue_view, name='revenue'),
    path('analytics/', views.analytics_view, name='analytics'),
    path('sales-team/', views.sales_team_view, name='sales_team'),
    path('settings/', views.settings_view, name='settings'),
]

