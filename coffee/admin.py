from django.contrib import admin
from .models import Coffee
from django_summernote.admin import SummernoteModelAdmin

class CoffeeAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

admin.site.register(Coffee, CoffeeAdmin)