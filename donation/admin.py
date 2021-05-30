from django.contrib import admin
from django.db import models
from .models import Coffee
# Register your models here.

class AdminCoffee(admin.ModelAdmin):
    list_display = ('id', 'name', 'amount', 'paid' , 'payment_date',)
    list_filter = ('payment_date',)

admin.site.register(Coffee, AdminCoffee)