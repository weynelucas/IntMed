from .models import Medicine
from django.forms import ModelForm

class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'presentation', 'laboratory', 'active_principle', 'pmc']
