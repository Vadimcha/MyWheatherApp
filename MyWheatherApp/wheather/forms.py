from django import forms
from .models import *

class GetCity(forms.Form):
    city = forms.CharField(max_length=100, label='')
    city.widget.attrs.update({ 'class': 'main_search', 'placeholder': 'Search Russian City...' })