from django.db import models

class UserFavorites(models.Model):

    user = models.ForeignKey("s4sUser", on_delete=models.CASCADE)
    sample = models.ForeignKey("Samples", on_delete=models.CASCADE)