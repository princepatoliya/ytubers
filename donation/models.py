from django.db import models

# Create your models here.

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    payment_id= models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name