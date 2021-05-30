from django.contrib import admin
from .models import HireTuber
# Register your models here.

class HAdmin(admin.ModelAdmin):
    ordering=('user_id',)
    list_display = ('user_id', 'first_name', 'last_name', 'tuber_id', 'tuber_name', 'messages')
    list_display_links = ('user_id', 'first_name', 'tuber_id', 'tuber_name',)
    list_filter = ('created_date', 'tuber_name',)
    

admin.site.register(HireTuber,HAdmin)
