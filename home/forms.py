from django import forms
from django.forms.models import ALL_FIELDS
from .models import beneficiary

class DateInput(forms.DateInput):
    input_type = 'date'


class beneficiaryForm(forms.ModelForm):
    class Meta:
        model=beneficiary
        fields=ALL_FIELDS
        widgets = {
            'date_of_birth': DateInput(),
        }
