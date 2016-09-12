from .models import DrugInteractionChecker
from django import forms
from IntMed.widgets import form_control

class DrugInteractionCheckerForm(forms.ModelForm):
    class Meta:
        model = DrugInteractionChecker
        fields = ['title', 'description', 'selected_drugs']
        widgets = {
            'title': forms.TextInput(attrs=form_control),
            'description': forms.Textarea(attrs=form_control),
            'selected_drugs': forms.MultipleHiddenInput(),
        }
