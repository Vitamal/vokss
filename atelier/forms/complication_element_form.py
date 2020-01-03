from django import forms
from atelier.models import ComplicationElement


class ComplicationElementForm(forms.ModelForm):
    class Meta:
        model = ComplicationElement
        fields = ['name', 'base_price', 'complexity', 'group']
