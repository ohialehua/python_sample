from django.db import models

# Create your models here.

class SampleAppModel(models.Model):
    itemname = models.CharField(max_length=100)
    itemvalue = models.IntegerField()