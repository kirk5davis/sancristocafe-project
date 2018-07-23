from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
	path('', views.emailView, name='contact'),
    path('success/', views.successView, name='success'),
]