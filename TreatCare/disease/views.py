from django.shortcuts import render
from .models import Disease
from .forms import DiseaseForm
from TreatCare.utils import query_service
from TreatCare.views import ListView, ModalFormView

class DiseaseListView(ListView):
    title = "Doenças"
    app_label = "disease"
    model_name = "Disease"
    fields = ["code", "description"]
    labels = ["Código", "Descrição"]

class DiseaseFormView(ModalFormView):
    title = "Adicionar Doença"
    subtitle = "Preencha o formulário abaixo:"
    form_class = DiseaseForm
