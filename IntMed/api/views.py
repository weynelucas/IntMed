from django.shortcuts import render
from IntMed.utils import query_service
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class ApiListView(APIView):
    def get(self, request, format=None):
        queryset = query_service.perform_lookup_query(self.model, request.GET.copy(), request.GET.get('q', ''))
        serializer = self.serializer_class(queryset, many=self.many)

        return Response(serializer.data)

    class Meta:
        abstract = True
