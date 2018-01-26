from django.db import models

# Create your models here.
class ServiceModel(models.Model):
    service = models.CharField(max_length=30)
    version = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
