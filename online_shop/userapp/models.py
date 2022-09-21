from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Account(models.Model):
    ism = models.CharField(max_length=20)
    jins = models.CharField(max_length=10, null=True, blank=True, default=None)
    city = models.CharField(max_length=30, null=True, blank=True, default=None)
    country = models.CharField(max_length=30, null=True, blank=True, default=None)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism
