from django.db import models

class UserFavorites(models.Model):

    user = models.ForeignKey("Users", on_delete=models.CASCADE)
    sample = models.ForeignKey("Samples", on_delete=models.CASCADE)