from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.deletion import CASCADE

class s4sUser(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sex = models.ForeignKey("Sexes", on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_image', height_field=None, max_length=None, width_field=None, null=True)