from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from atelier.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'product', 'fabric', 'processing_category', 'complication_elements', 'allowance_discount',
                  'order_date', 'deadline']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save order'))
