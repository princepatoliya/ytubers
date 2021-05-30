from ckeditor.fields import RichTextField
from django.contrib import messages
from django.db import models
from datetime import datetime

# Create your models here.

class HireTuber(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)

    tuber_id = models.IntegerField()
    tuber_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    messages = RichTextField()
    
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email_id
