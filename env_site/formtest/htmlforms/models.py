from django.db import models


# Create your models here.
class Entry(models.Model):
 name = models.CharField(max_length=200)

class JsonEntry(models.Model):
    entry = models.JSONField()



