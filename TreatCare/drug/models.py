from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Drug(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)

    class Meta:
        verbose_name = _('drug')
