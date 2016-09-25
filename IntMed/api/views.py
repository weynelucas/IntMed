from django.shortcuts import render, get_object_or_404
from IntMed.utils import query_service
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from django.utils.translation import ugettext_lazy as _
# Create your views here.

class ApiListView(APIView):
    permission_classes = (IsAuthenticated,)
    has_owner = False

    def get(self, request, format=None):
        params = request.GET.copy()
        queryset = query_service.perform_lookup_query(self.model, params)

        if self.has_owner:
            queryset = queryset.filter(owner__id=request.user.id)

        serializer = self.serializer_class(queryset, many=self.many)

        return Response(serializer.data)

    class Meta:
        abstract = True

class ApiDetailsView(APIView):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    delete_feedback_message = _("Successfully removed")

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = self.serializer_class(obj)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = self.serializer_class(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        context = {
            'feedbackMessage': self.delete_feedback_message,
        }
        return Response(context)

    class Meta:
        abstract = True
