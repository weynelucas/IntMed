from django.db import models

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(null=False, blank=False, max_length=250)
    laboratory = models.CharField(null=True, blank=True, max_length=250)
    presentation = models.CharField(null=True, blank=True, max_length=250)
    active_principle = models.CharField(null=True, blank=True, max_length=250)
    pmc = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'medicamento'
        verbose_name_plural = 'medicamentos'
