from django.db import models

class SampleRatings(models.Model):

    user = models.ForeignKey("s4sUser", on_delete=models.CASCADE, related_name="s4sUser")
    sample = models.ForeignKey("Samples", on_delete=models.CASCADE)
    rating = models.CharField(max_length=50)
    color= models.CharField(max_length=50)
    loudness= models.CharField(max_length=50)