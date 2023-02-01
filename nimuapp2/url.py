from django.contrib import admin
from django.urls import path
from . import views

app_name = 'nimuapp2'

urlpatterns = [
    path('home1/', views.home1, name='home1'),
    path('home1/update1/<pk>',views.update1, name='update1')
    
]