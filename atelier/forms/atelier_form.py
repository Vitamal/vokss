from django import forms
from atelier.models import Atelier


class AtelierForm(forms.ModelForm):
    class Meta:
        model = Atelier
        fields = ['name']
