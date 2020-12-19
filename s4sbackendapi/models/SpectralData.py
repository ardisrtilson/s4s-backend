from django.db import models

class Spectra(models.Model):

    sample = models.ForeignKey("Samples", on_delete=models.CASCADE)
    gain = models.CharField(max_length=30)
    resonance = models.CharField(max_length=30)