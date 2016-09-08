from django.conf.urls import url
from .drug_interaction.connection import get_drug_interactions, get_multiple_drugs_interactions
from . import views

urlpatterns = [
    url(r'^single/', views.DrugInteractionListView.as_view(query_callback=get_drug_interactions)),
    url(r'^multiple/', views.DrugInteractionListView.as_view(arg_is_list=True, query_callback=get_multiple_drugs_interactions)),
]
