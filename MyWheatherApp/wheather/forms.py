from django import forms

class GetCity(forms.Form):
    citt = forms.CharField(max_length=100)