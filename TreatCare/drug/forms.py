from .models import Drug
from django.forms import ModelForm, TextInput, NumberInput

form_control = {'class': 'form-control'}


class DrugForm(ModelForm):
    class Meta:
        model = Drug
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs=form_control),
        }
        labels = {
            'name': 'Nome',
        }
