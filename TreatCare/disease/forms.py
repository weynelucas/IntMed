from .models import Disease
from django.forms import ModelForm, TextInput

form_control = {'class': 'form-control'}

class DiseaseForm(ModelForm):
    class Meta:
        model = Disease
        fields = ['code', 'description']
        widgets = {
            'code': TextInput(attrs=form_control),
            'description': TextInput(attrs=form_control),
        }
        labels = {
            'code': 'Código',
            'description': 'Descrição',
        }
