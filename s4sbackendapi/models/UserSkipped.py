from django.db import models

class UserSkipped(models.Model):

    user = models.ForeignKey("s4sUser", on_delete=models.CASCADE)
    sample = models.ForeignKey("Samples", on_delete=models.CASCADE)