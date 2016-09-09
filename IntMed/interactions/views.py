from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
# Create your views here.

class DrugInteractionListView(View):
    arg_name = 'drug'
    arg_is_list = False
    query_callback = None

    def get(self, request):
        if self.arg_is_list:
            arg = request.GET.getlist(self.arg_name)
        else:
            arg = request.GET.get(self.arg_name)

        result = self.query_callback(arg)
        result_dict = [dict(record) for record in result]
        return JsonResponse(result_dict, safe=False)
