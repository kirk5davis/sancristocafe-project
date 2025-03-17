from django.urls import path

from . import views

urlpatterns = [
	path('', views.news, name='news'),
	# path('blog/', views.blog, name="blog"),
	path('<int:blog_id>/', views.post_details, name='post_details'),
	path('newsletter/', views.newsletter, name='newsletter'),
	path('archives/', views.archives, name='archives'),
	path('archives/<str:type>/<int:archive_id>/', views.archive_details, name='archive_details'),
]
