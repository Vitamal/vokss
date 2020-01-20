from django import forms
from django.forms import CheckboxSelectMultiple

from atelier.models import Order, ComplicationElement


class OrderForm(forms.ModelForm):
    complication_elements = forms.CheckboxSelectMultiple()

    class Meta:
        model = Order
        fields = ['client', 'product', 'fabric', 'processing_category', 'complication_elements', 'allowance_discount',
                  'performer', 'order_date', 'deadline', 'is_closed']
        widgets = {
            'complication_elements': CheckboxSelectMultiple(),
            'allowance_discount': CheckboxSelectMultiple()
        }
