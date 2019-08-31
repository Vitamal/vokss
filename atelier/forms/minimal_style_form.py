from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit
from atelier.models import MinimalStyle


class MinimalStyleForm(forms.ModelForm):
    class Meta:
        model = MinimalStyle
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Save minimal_style'))

