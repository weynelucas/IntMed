from rest_framework import serializers
from .models import DrugInteractionChecker
from drug.serializers import DrugSerializer

class DrugInteractionCheckerSerializer(serializers.ModelSerializer):
    selected_drugs = DrugSerializer(read_only=True, many=True)
    class Meta:
        model = DrugInteractionChecker
        fields = ('id', 'title', 'description', 'uses', 'created_at', 'selected_drugs')
