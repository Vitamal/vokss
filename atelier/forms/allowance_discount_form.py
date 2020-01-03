from django import forms
from atelier.models import AllowanceDiscount


class AllowanceDiscountForm(forms.ModelForm):
    class Meta:
        model = AllowanceDiscount
        fields = ['name', 'coefficient', 'label']

