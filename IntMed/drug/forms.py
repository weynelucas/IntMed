from .models import Drug
from django import forms
from IntMed.widgets import form_control

class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ['name', 'action']
        widgets = {
            'name': forms.TextInput(attrs=form_control),
            'action': forms.TextInput(attrs=form_control),
        }
