from django.urls import path
from .views import generate_pdf, barcode_image_view, generate1_pdf, get_images, GeneratePDF
from . import views

urlpatterns = [
    path('', views.detect_barcode, name='detect_barcode'),
   # path('', views.detect_barcode, name='detect_barcodes'),
    path('camera_feed', views.camera_feed, name='camera_feed'),
    path('detect_barcodes/', views.detect_barcode, name='detect_barcodes-detect_barcodes'),
    path('get_customer_details/', views.get_customer_details, name='get_customer_details'),
    path('detect_inverter/', views.detect_inverter, name='detect_barcodes-detect_inverter'),
    path('get_inverter_details/', views.get_inverter_details, name='get_inverter_details'),
    #path('barcodepdf/<int:pk>', views.pdf_barcode_create, name='detect_barcodes-barcodepdf'),
    #path('generate-pdf/', views.generate_pdf, name='generate-pdf'),
    path('detect_barcodes1/', views.upload_barcode, name='detect_barcodes-upload_barcode'),
    path('ajax/handle_upload/', views.ajax_handle_upload, name='detect_barcodes-ajax_handle_upload'),
    path('barcodepdf/', barcode_image_view, name='detect_barcodes-barcodepdf'),
    path('get_images/', get_images, name='detect_barcodes-get_images'),
    #path('generate_pdf/', generate1_pdf, name='detect_barcodes-generate_pdf'),
    path('search/', views.search_view, name='detect_barcodes-search'),
    path('generate_pdf/', views.GeneratePDF, name='detect_barcodes-generate_pdf'),
    path('edit_barcode/', views.editbarcode, name='detect_barcodes-edit_barcode'),
    path('editbarcode/', views.editbarcode, name='editbarcode'),  # The URL pattern for your editbarcode view

    path('delete_barcode/', views.deletebarcode, name='detect_barcodes-delete_barcode'),
    path('deletebarcode/', views.deletebarcode, name='deletebarcode'),  # The URL pattern for your editbarcode view

]
