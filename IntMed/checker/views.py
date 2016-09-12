from django.shortcuts import render
from IntMed.views import ModalCreateFormView
from .forms import DrugInteractionCheckerForm
from django.utils.translation import ugettext_lazy as _

class DrugInteractionCheckerFormView(ModalCreateFormView):
    title = _('Save Drug Interaction')
    subtitle = _('Save your most searched multiple drugs interactions to check them more easily in the future.')
    form_class = DrugInteractionCheckerForm
