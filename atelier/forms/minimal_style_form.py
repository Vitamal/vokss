from django import forms
from atelier.models import MinimalStyle


class MinimalStyleForm(forms.ModelForm):
    class Meta:
        model = MinimalStyle
        fields = ['name', 'group']

