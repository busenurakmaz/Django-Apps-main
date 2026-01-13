from django.urls import path
from . import views

app_name = 'online_therapy'

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.therapy_form, name='form'),
    path('success/', views.success, name='success'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('psychologist-dashboard/', views.psychologist_dashboard, name='psychologist_dashboard'),
    path('form/<int:pk>/', views.form_detail, name='form_detail'),
]
