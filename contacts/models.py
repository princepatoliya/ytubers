from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

# this class info for website like website-email,phone social account links
class contact_info(models.Model):
  email_id = models.CharField(max_length=255)
  phone_no = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  facebook = models.CharField(max_length=255)
  instagram = models.CharField(max_length=255)
  twitter = models.CharField(max_length=255)
  youtube = models.CharField(max_length=255)

  about_photo = models.ImageField(default='', upload_to='media/about/%Y/%M/')
  about_project = RichTextField(default='')

  def __str__(self):
      return self.email_id
    

# this for contact_form on contactus page
class contact_form(models.Model):
  user_id = models.IntegerField()
  name = models.CharField(max_length=255)
  contactno = models.CharField(max_length=255)
  emailid =models.CharField(max_length=255)
  companyname = models.CharField(max_length=255)
  subject = models.CharField(max_length=255)
  message = models.CharField(max_length=255)
  created_date = models.DateTimeField(default=datetime.now, blank = True)

  def __str__(self):
    return self.name