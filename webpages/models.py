from django.db import models
# Create your models here.

# model for teams info
class Team(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  role = models.CharField(max_length=80)
  insta_link = models.CharField(max_length=255)
  linkedin_link = models.CharField(max_length=255)
  youtube_link = models.CharField(default = '', max_length=255)
  photo = models.ImageField(upload_to='media/team/%Y/%M/%D/')
  created_date = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.first_name 

# model for sliders on home page
class Slider(models.Model):
  headline = models.CharField(max_length=255)
  subtitle = models.CharField(max_length=255)
  button = models.CharField(max_length=255)
  links = models.CharField(default = '', max_length=255)
  photo = models.ImageField(default='', upload_to='media/slider/%Y/')
  created_date = models.DateField(auto_now_add=True)
  

  def __str__(self):
    return self.headline
  



