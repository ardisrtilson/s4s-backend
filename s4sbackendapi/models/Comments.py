from django.db import models

class Comments(models.Model):

    user = models.ForeignKey("Users", on_delete=models.CASCADE)
    sample = models.ForeignKey("Samples", on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    date_added = models.CharField(max_length=30)