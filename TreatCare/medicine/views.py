from django.shortcuts import render
from .models import Medicine
from .forms import MedicineForm
from TreatCare.utils import query_service
from TreatCare.views import ListView, ModalCreateFormView
from TreatCare.decorators import ajax_required

class MedicineListView(ListView):
    title = "Medicamentos"
    app_label = "medicine"
    model_name = "Medicine"
    fields = ["name", "presentation", "laboratory", "active_principle", "pmc"]
    labels = ["Medicamento", "Apresentação", "Laboratório", "Princípio Ativo", "PMC R$"]


class MedicineFormView(ModalCreateFormView):
    title = "Adicionar Medicamento"
    form_class = MedicineForm
