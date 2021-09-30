from django import forms
from .models import Program


class contactform(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name']
