from .models import DrugInteractionChecker
from django import forms
from IntMed.widgets import form_control

class DrugInteractionCheckerForm(forms.ModelForm):
    class Meta:
        model = DrugInteractionChecker
        fields = ['title', 'owner', 'selected_drugs']
        widgets = {
            'title': forms.TextInput(attrs=form_control),
            'selected_drugs': forms.MultipleHiddenInput(),
            'owner': forms.HiddenInput(),
        }
