from django.db import models

class Sexes(models.Model):

    sex = models.CharField(max_length=30)