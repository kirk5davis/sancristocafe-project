from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog, Newsletter, ArchivedFile


# apply summernote to only the TextField for the post content
class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Newsletter)
admin.site.register(ArchivedFile)