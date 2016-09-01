from .models import Medicine
from django.forms import ModelForm, TextInput, NumberInput

form_control = {'class': 'form-control'}


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'
        widgets = {
            'pmc': NumberInput(attrs=form_control),
            'name': TextInput(attrs=form_control),
            'laboratory': TextInput(attrs=form_control),
            'presentation': TextInput(attrs=form_control),
            'active_principle': TextInput(attrs=form_control),
        }
        labels = {
            'pmc': 'PMC',
            'name': 'Nome',
            'laboratory': 'Laboratório',
            'presentation': 'Apresentação',
            'active_principle': 'Princípio ativo',
        }
