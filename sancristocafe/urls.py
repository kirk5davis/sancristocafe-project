"""sancristocafe URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import coffee.views

admin.site.site_header = "San Cristobal Coffee Importers Website Administration Portal"
admin.site.site_title = "San Cristobal Coffee Importers Web Administration"
admin.site.index_title = "Welcome to San Cristobal Coffee Importers Website Admin Page"

urlpatterns = [
    path('scci_admin_portal/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('captcha/', include('captcha.urls')),
    path('', coffee.views.home, name='home'),
    path('about/', coffee.views.about, name='about'),
    path('coffees/', coffee.views.coffees, name='coffees'),
    path('source-work/', coffee.views.source_work, name='source-work'),
    path('source-work/mexico', coffee.views.source_mexico, name="mexico"),
    path('source-work/ethiopia', coffee.views.source_ethiopia, name="ethiopia"),
    path('traceability/', coffee.views.traceability, name='traceability'),
    path('news/', include('blog.urls'), name='news'),
    path('contact/', include('contact.urls'), name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
