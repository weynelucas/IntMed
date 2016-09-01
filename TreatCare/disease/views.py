from django.shortcuts import render
from .models import Disease
from .forms import DiseaseForm
from TreatCare.utils import query_service
from TreatCare.views import ListView, ModalCreateFormView

class DiseaseListView(ListView):
    title = "Doenças"
    app_label = "disease"
    model_name = "Disease"
    fields = ["code", "description"]
    labels = ["Código", "Descrição"]
    enable_create = False

class DiseaseFormView(ModalCreateFormView):
    title = "Adicionar Doença"
    main_property = "description"
    form_class = DiseaseForm
