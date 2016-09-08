from django.shortcuts import render
from .models import Drug
from .forms import DrugForm
from IntMed.views import ListView, ModalCreateFormView
from django.utils.translation import ugettext_lazy as _


class DrugListView(ListView):
    app_label = "drug"
    model_name = "Drug"

    fields = ["name", "action"]
    enable_create = True

    title = _("Drugs")
    labels = [_("Drug"), _("Action")]


class DrugFormView(ModalCreateFormView):
    title = _("Add Drug")
    form_class = DrugForm


def interactions(request):
    return render(request, 'drug/interactions.html')

def single_interactions(request):
    return render(request, 'drug/single_interactions.html')
