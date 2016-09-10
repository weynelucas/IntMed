from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Drug(models.Model):
    name = models.CharField(verbose_name=_('name'), null=False, blank=False, max_length=255)
    action = models.CharField(verbose_name=_('action'), null=False, blank=False, max_length=125)
    class Meta:
        verbose_name = _('drug')


class CheckerResult(models.Model):
    title = models.CharField(verbose_name=_('title'), null=True, blank=True, max_length=255)
    description = models.CharField(verbose_name=_('description'), null=True, blank=True, max_length=750)
    drugs = models.ManyToManyField(Drug)
