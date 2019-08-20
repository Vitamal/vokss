from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from atelier.models import MyClient

class ClientForm(forms.ModelForm):
    class Meta:
        model = MyClient
        fields = ('first_name', 'last_name', 'tel_number', 'place')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))
