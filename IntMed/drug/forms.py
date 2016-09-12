from .models import Drug
from django import forms
from IntMed.widgets import form_control

class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs=form_control),
            'action': formsTextInput(attrs=form_control),
        }
