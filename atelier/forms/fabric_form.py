from django import forms
from atelier.models import Fabric


class FabricForm(forms.ModelForm):
    class Meta:
        model = Fabric
        fields = ['name', 'group', 'complexity_factor']


