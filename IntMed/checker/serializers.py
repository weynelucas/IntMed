from rest_framework import serializers
from .models import DrugInteractionChecker
from drug.serializers import DrugSerializer
from accounts.serializers import UserSerializer

class DrugInteractionCheckerSerializer(serializers.ModelSerializer):
    selected_drugs = DrugSerializer(read_only=True, many=True)
    owner = UserSerializer(read_only=True)
    class Meta:
        model = DrugInteractionChecker
        fields = ('id', 'title', 'uses', 'created_at', 'owner', 'selected_drugs')
