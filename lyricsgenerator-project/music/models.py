from django.db import models

# Create your models here.

class Music(models.Model):
    artist = models.CharField(max_length=100)
    songName = models.CharField(max_length=100)
    lyrics = models.CharField(max_length=10000)