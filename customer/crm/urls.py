from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    path('leads/', views.leads_list, name='leads_list'),
    path('leads/<int:pk>/', views.lead_detail, name='lead_detail'),
    path('pipeline/', views.pipeline_view, name='pipeline'),
    path('api/lead/<int:pk>/stage/', views.update_lead_stage, name='update_lead_stage'),
]

