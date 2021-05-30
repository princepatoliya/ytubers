from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.

class Youtuber(models.Model):

    crew_choices = (
        ('solo', 'solo'),
        ('small', 'small'),
        ('large', 'large'),
    )

    camera_choices = (
        ('canon', 'canon'),
        ('nikon', 'nikon'),
        ('sony', 'sony'),
        ('fuji', 'fuji'),
        ('red', 'red'),
        ('panasonic', 'panasonic'),
        ('other', 'other'),
    )

    category_choices = (
        ('code', 'code'),
        ('mobile_review', 'mobile_review'),
        ('vlog', 'vlog'),
        ('comedy', 'comedy'),
        ('gaming', 'gaming'),
        ('film_making', 'film_making'),
        ('cooking', 'cooking'),
        ('rosting', 'rosting'),
    )

    def __str__(self):
        return self.name


    name = models.CharField(max_length=255)
    emailid = models.CharField(default = '', max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/ytubers/%Y/%m')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices = crew_choices ,max_length=255)
    camera_type = models.CharField(choices = camera_choices ,max_length=255)
    subs_count = models.CharField(max_length=255)
    category = models.CharField(choices = category_choices ,max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank = True)

    


