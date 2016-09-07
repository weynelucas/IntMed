from django.shortcuts import render
from .models import Drug
from .forms import DrugForm
from IntMed.utils import query_service
from IntMed.views import ListView, ModalCreateFormView
from neo4j.v1 import GraphDatabase, basic_auth
from django.http import JsonResponse
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

def perform_interactions(request):
    if request.method == 'POST':
         params = request.POST
    else:
        params = request.GET

    drugs = params.getlist('drug')

    driver = GraphDatabase.driver("bolt://54.152.213.214/browser/", auth=basic_auth("neo4j", "ufc=1890"))
    session = driver.session()
    cypher_query =  """
                        MATCH (d:DRUG)
                        WHERE d.name IN %s
                        WITH COLLECT(d) as ds
                        MATCH (x)-[r]-(y)
                        WHERE x in ds AND y in ds
                        RETURN DISTINCT type(r) as type, r.evidence as evidence, r.action as action, r.explanation as explanation, startNode(r).name as startNode, endNode(r).name as endNode
                    """ % (str(drugs))

    result = session.run(cypher_query)
    result_dict = [dict(record) for record in result]
    return JsonResponse(result_dict, safe=False)
