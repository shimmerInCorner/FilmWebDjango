from django.db import models


# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.URLField(max_length=1000)
    duration = models.IntegerField()
    grade = models.FloatField()
    type = models.CharField(max_length=100)
    watch_url = models.URLField(max_length=1000, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.type
