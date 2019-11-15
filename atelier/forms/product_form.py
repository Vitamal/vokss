from django import forms

from atelier.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'name',
            'minimal_style',
            'base_price'
        ]
