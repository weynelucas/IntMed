from django.shortcuts import render, get_object_or_404
from IntMed.utils.request_service import get_params
from django.contrib.auth.decorators import login_required
from drug.models import Drug
from drug.serializers import DrugSerializer


@login_required
def index(request):
    context = {
        'active': 'multiple',
    }
    return render(request, "interactions/index.html", context)

@login_required
def single(request, id = None):
    context = {}
    params = get_params(request)
    drugId = params.get('drugId')

    if id:
        drug = get_object_or_404(Drug, pk=id)
        context['drug'] = DrugSerializer(drug).data

    context['active'] = 'single'

    return render(request, "interactions/single.html", context)
