from django.shortcuts import render
from .models import Disease
from TreatCare.utils import query_service
from TreatCare.views import ListView

class DiseaseListView(ListView):
    title = "Doenças"
    app_label = "disease"
    model_name = "Disease"
    fields = ["code", "description"]
    labels = ["Código", "Descrição"]
