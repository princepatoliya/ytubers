from django.contrib import admin
from .models import contact_info, contact_form

# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email_id', 'phone_no', 'address')

class formAdmin(admin.ModelAdmin):
    ordering = ('user_id',)
    list_display = ('user_id', 'name', 'companyname', 'subject',)
    list_display_links = ('user_id', 'name',)
    list_filter = ('companyname', 'created_date')
    
admin.site.register(contact_info, contactAdmin)
admin.site.register(contact_form, formAdmin)