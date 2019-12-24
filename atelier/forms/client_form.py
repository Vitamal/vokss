from django import forms
from atelier.models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'tel_number', 'place']

