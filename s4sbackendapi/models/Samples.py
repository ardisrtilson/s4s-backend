from django.db import models

class Samples(models.Model):

    uploader = models.ForeignKey("Users", on_delete=models.CASCADE)
    rating = models.CharField(max_length=50)
    color= models.CharField(max_length=50)
    loudness= models.CharField(max_length=50)
    audio_url = models.CharField(max_length=250)
    date_added = models.CharField(max_length=30)
