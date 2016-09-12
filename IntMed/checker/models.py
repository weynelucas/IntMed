from django.db import models
from drug.models import Drug
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class DrugInteractionChecker(models.Model):
    title = models.CharField(blank=True, null=True, max_length=150, help_text=_('Title (Optional)'))
    description = models.CharField(blank=True, null=True, max_length=500, help_text=_('Description (Optional)'))
    uses = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    selected_drugs = models.ManyToManyField(Drug)

    class Meta:
        verbose_name = _('drug interaction')
