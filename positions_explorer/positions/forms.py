from django import forms

from . import models


class AxisValuesForm(forms.Form):

    values = forms.ModelMultipleChoiceField(
        models.AxisValues.objects.none(),
        to_field_name='value',
        widget=forms.CheckboxSelectMultiple
    )
    contributor = forms.ModelChoiceField(
        models.Contributor.objects.none(),
        widget=forms.HiddenInput
    )

    def __init__(self, *args, **kwargs):
        axis = kwargs.pop('axis')
        contributor_pk = kwargs.pop('contributor_pk', None)
        super(AxisValuesForm, self).__init__(*args, **kwargs)
        self.fields['values'].queryset = models.AxisValues.objects.filter(axis=axis)
        if contributor_pk:
            self.fields['contributor'].queryset = models.Contributor.objects.filter(pk=contributor_pk)
            self.fields['contributor'].initial = self.fields['contributor'].queryset.first()
