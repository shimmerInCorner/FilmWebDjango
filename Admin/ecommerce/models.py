from django.db import models


# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.URLField(max_length=1000)
    duration = models.IntegerField()
    grade = models.FloatField(default=0.0)
    type = models.CharField(max_length=100)
    watch_url = models.URLField(max_length=1000, null=True)
    price = models.IntegerField()
    features = models.CharField(max_length=200, default='Default')
    description = models.CharField(max_length=1000, default='None')
    meta_description = models.CharField(max_length=1000, default='None')
    country = models.CharField(max_length=100, default='Unknown')
    restriction = models.CharField(max_length=100, default='G')

