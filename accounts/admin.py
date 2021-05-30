from django.contrib import admin
from .models import *

# Register your models here
class AdminProfile(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_verified', 'created_at')
    list_filter = ('is_verified', 'created_at')
    list_editable = ('is_verified',)

admin.site.register(Profile,AdminProfile)