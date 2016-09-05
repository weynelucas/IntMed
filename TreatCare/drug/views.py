from django.shortcuts import render
from .models import Drug
from .forms import DrugForm
from TreatCare.utils import query_service
from TreatCare.views import ListView, ModalCreateFormView
from neo4j.v1 import GraphDatabase, basic_auth
from django.http import JsonResponse


class DrugListView(ListView):
    title = "Medicamentos"
    app_label = "drug"
    model_name = "Drug"
    fields = ["name"]
    labels = ["Medicamento"]


class DrugFormView(ModalCreateFormView):
    title = "Adicionar Medicamento"
    form_class = DrugForm

def interactions(request):
    return render(request, 'drug/interactions.html')

def perform_interactions(request):
    if request.method == 'POST':
         params = request.POST
    else:
        params = request.GET

    drugs = params.getlist('drug')
    print(drugs)

    driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "password"))
    session = driver.session()
    cypher_query =  """
                        MATCH (d:DRUG)
                        WHERE d.name IN %s
                        WITH COLLECT(d) as ds
                        MATCH (x)-[r]-(y)
                        WHERE x in ds AND y in ds
                        RETURN DISTINCT type(r) as type, r.explanation as explanation, startNode(r).name as startNode, endNode(r).name as endNode
                    """ % (str(drugs))

    result = session.run(cypher_query)
    result_dict = [dict(record) for record in result]
    print(result_dict)
    return JsonResponse(result_dict, safe=False)
