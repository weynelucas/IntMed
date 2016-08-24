from django.shortcuts import render
from .models import Medicine
from TreatCare.utils import query_service

# Create your views here.
def list(request):
    params = request.GET.copy()
    objects = query_service.perform_query(app_label='medicine', model_name='Medicine', params=params)
    objects = query_service.paginate_list(objects, params, 50)
    context = {
        'objects': objects,
    }
    return render(request, 'medicine/list.html', context)
