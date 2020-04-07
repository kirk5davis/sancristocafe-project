from django.contrib import admin
from .models import Coffee, OfferingsList, Banner
from django_summernote.admin import SummernoteModelAdmin

class CoffeeAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

class BannerAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Coffee, CoffeeAdmin)
admin.site.register(OfferingsList)
admin.site.register(Banner, BannerAdmin)