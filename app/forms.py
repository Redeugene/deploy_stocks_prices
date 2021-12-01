from django import forms
from .models import *


class LocationChoiceField(forms.Form):
    name = forms.CharField(max_length=100)
    locations = forms.ModelChoiceField(
        queryset=stock_params.objects.values_list("name", flat=True).distinct(),
        empty_label=None
    )

class UserForm(forms.Form):
    name= forms.CharField(max_length=100)
