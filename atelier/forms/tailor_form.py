from django import forms
from atelier.models import Tailor


class TailorForm(forms.ModelForm):
    class Meta:
        model = Tailor
        fields = ('first_name', 'last_name', 'email', 'atelier')
        # fields = '__all__'
