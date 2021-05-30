from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    
    def myphoto(self, object):
        return format_html('<img src="{}" width="50">'.format(object.photo.url))
    
    ordering = ('id',)

    list_display = ('id', 'myphoto', 'first_name', 'role', 'created_date',)
    list_display_links = ('first_name', 'id',)
    search_fields = ('first_name', 'role')
    list_filter = ('role','created_date')



class SlideAdmin(admin.ModelAdmin):
    
    def slidephoto(self, object):
        return format_html('<img src="{}" width="100" height="25">'.format(object.photo.url))
    
    ordering = ('id',)
    list_display = ('id', 'slidephoto', 'headline', 'links',)
    list_filter = ('created_date',)


admin.site.register(Slider, SlideAdmin)
admin.site.register(Team, TeamAdmin)
