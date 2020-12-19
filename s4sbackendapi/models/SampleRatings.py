from django.db import models

class SampleRatings(models.Model):

    user = models.ForeignKey("Users", on_delete=models.CASCADE, related_name="user")
    sample = models.ForeignKey("Samples", on_delete=models.CASCADE)
    rating = models.CharField(max_length=50)