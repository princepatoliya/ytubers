from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html
# Register your models here.

class YAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="50">'.format(object.photo.url))

        
    ordering = ('id',)
    list_display = ('id','myphoto', 'name', 'subs_count', 'is_featured')
    search_fields = ('name', 'camera_type')
    list_filter = ('created_date', 'city', 'camera_type',)
    list_display_links = ('id', 'name')
    list_editable = ('is_featured',)




admin.site.register(Youtuber, YAdmin)

