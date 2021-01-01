from django.db import models

class Samples(models.Model):

    uploader = models.ForeignKey("s4sUser", on_delete=models.CASCADE)
    audio_url = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    date_added = models.CharField(max_length=30)
    sample_image = models.ImageField(upload_to='sample_image', height_field=None, max_length=None, width_field=None, null=True)
