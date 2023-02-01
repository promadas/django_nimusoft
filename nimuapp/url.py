from django.contrib import admin
from django.urls import path
from . import views

app_name = 'nimuapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form_submit, name='form'),
    path('form/update/<pk>',views.update, name='update'),
    path('form/delete/<pk>',views.delete, name='delete'),
    
    
]