import ast
from django.shortcuts import render
from .models import Drug
from .forms import DrugForm
from IntMed.views import ListView, ModalCreateFormView
from django.utils.translation import ugettext_lazy as _

class DrugListView(ListView):
    app_label = "drug"
    model_name = "Drug"
    fields = ["name", "action"]
    labels = [_("Drug"), _("Action")]
    title = _("Drugs")
    enable_create = False


class DrugFormView(ModalCreateFormView):
    title = _("Add Drug")
    form_class = DrugForm

def interactions(request):
    return render(request, 'drug/interactions.html')
