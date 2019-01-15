"""sancristocafe URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import coffee.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', coffee.views.home, name='home'),
    path('about/', coffee.views.about, name='about'),
    path('coffees/', coffee.views.coffees, name='coffees'),
    path('source-work/', coffee.views.source_work, name='source-work'),
    path('news/', include('blog.urls'), name='news'),
    path('contact/', include('contact.urls'), name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
