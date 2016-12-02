from django.db import models
from django.contrib.auth.models import User
from drug.models import Drug
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class DrugInteractionChecker(models.Model):
    title = models.CharField(blank=True, null=True, max_length=150, help_text=_('Title (Optional)'))
    uses = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    selected_drugs = models.ManyToManyField(Drug)
    owner = models.ForeignKey(User)

    class Meta:
        verbose_name = _('drug interaction')
