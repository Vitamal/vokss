from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit
from atelier.models import ComplicationElement


class ComplicationElementForm(forms.ModelForm):
    class Meta:
        model = ComplicationElement
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Save complication_element'))

