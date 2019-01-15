from django.urls import path

from . import views

urlpatterns = [
	path('', views.blogs, name='news'),
	path('<int:blog_id>/', views.post_details, name='post_details'),
	path('archives/', views.archives, name='archives'),
	path('archives/<str:type>/<int:archive_id>/', views.archive_details, name='archive_details'),
]
