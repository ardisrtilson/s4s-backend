from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):

    sex = models.ForeignKey("Sexes", on_delete=models.CASCADE)