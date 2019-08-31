from django import forms
from atelier.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        minimal_style = forms.CharField(widget=forms.Textarea)


