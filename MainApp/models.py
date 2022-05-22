from django.db import models

# Create your models here.
class Country_o(models.Model):
   country  = models.CharField(max_length=100)
   languages = models.CharField(max_length=100)
