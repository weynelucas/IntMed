from .models import Drug, CheckerResult
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, TextInput, Textarea, HiddenInput, ModelMultipleChoiceField, MultipleHiddenInput

form_control = {'class': 'form-control'}


class DrugForm(ModelForm):
    class Meta:
        model = Drug
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs=form_control),
            'action': TextInput(attrs=form_control),
        }


class CheckerResultForm(ModelForm):
    # drugs = NotValidatedMultipleChoiceFiled(queryset=Drug.objects.all())
    class Meta:
        model = CheckerResult
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs=form_control),
            'description': Textarea(attrs=form_control),
            'drugs': MultipleHiddenInput(),
        }
