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

    class Meta:
        model = CheckerResult
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs=form_control),
            'description': Textarea(attrs=form_control),
            'drugs': MultipleHiddenInput(),
        }

    def  __init__(self, *args, **kwargs):
        super(CheckerResultForm, self).__init__(*args, **kwargs)
        print('_________________________________________________\n\n')
        print(kwargs)
        print(args)

    def save(self, commit=True):
        print(self.cleaned_data)
        interaction_id = self.cleaned_data['interaction']
        interaction_ation = self.cleaned_data[interaction_id + '_action']
        interaction_evidence = self.cleaned_data[interaction_id + '_evidence']
        interaction_explanation = self.cleaned_data[interaction_id + '_explanation']

        print(interaction_id)
        print(interaction_action)
        print(interaction_evidence)
        print(interaction_explanation)

        super(CheckerResultForm, self).save()
