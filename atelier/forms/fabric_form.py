from django import forms
from atelier.models import Fabric


class FabricForm(forms.ModelForm):
    class Meta:
        model = Fabric
        fields = '__all__'


