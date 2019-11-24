from django import forms
from atelier.models import Tailor


class TailorForm(forms.ModelForm):
    class Meta:
        model = Tailor
        fields = '__all__'
