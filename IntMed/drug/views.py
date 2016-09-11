import json
import ast
from django.shortcuts import render
from .models import Drug
from .forms import DrugForm, CheckerResultForm
from django.http import JsonResponse, HttpResponse
from IntMed.views import ListView, ModalCreateFormView
from django.utils.translation import ugettext_lazy as _
from IntMed.checker_report import generate_checker_report

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

def export(request):
    response = HttpResponse(content_type='application/pdf')
    filename = 'Relatorio_'
    response['Content-Disposition'] ='attachement; filename=%s.pdf' % (filename)

    pdf = generate_checker_report(ast.literal_eval(request.GET.get('pdfModel')))
    response.write(pdf)
    return response
