from django.shortcuts import render
from .models import Drug
from .forms import DrugForm, CheckerResultForm
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

class CheckerResultFormView(ModalCreateFormView):
    title = _("Add Drug")
    form_class = CheckerResultForm
    append_language_code = True
    url = "/drug/save_result/"


def interactions(request):
    return render(request, 'drug/interactions.html')
