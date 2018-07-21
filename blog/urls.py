from django.urls import path

from . import views

urlpatterns = [
	path('', views.blogs, name='blog'),
	path('<int:blog_id>/', views.post_details, name='post_details'),
]
