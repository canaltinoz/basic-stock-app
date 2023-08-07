from django.forms import ModelForm
from django import forms
from .models import Flavour

VARIETY_CHOICES = [
    ("Flavour","flavour"),
]
class UploadForm(ModelForm):
    name=forms.TextInput()
    variety=forms.ChoiceField(choices=VARIETY_CHOICES)

    class Meta:
        model=Flavour
        fields=['name','variety']

class GetForm(ModelForm):
    class Meta:
        model=Flavour
        fields=('total',)
        labels={'total':'Total'}
        widgets={
            'total':forms.NumberInput(),
        }