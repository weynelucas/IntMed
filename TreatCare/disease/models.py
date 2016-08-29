from django.db import models

# Create your models here.
class Disease(models.Model):
    code = models.CharField(null=False, blank=False, max_length=10)
    description = models.CharField(null=False, blank=False, max_length=455)
