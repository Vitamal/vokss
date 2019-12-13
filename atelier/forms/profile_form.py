from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UserForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(max_length=50)
    password2 = forms.CharField(max_length=50)
    is_tailor = forms.BooleanField(required=False)

    # def clean(self):
    #     super().clean()
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
    #     if password1 and password2:
    #         if password1 != password2:
    #             raise forms.ValidationError(
    #                 _("The two password fields didn't match. ")
    #             )
    #
    # def is_valid(self):
    #     valid = super(UserForm).is_valid()
    #     if not valid:
    #         return valid
    #     if self.cleaned_data.get("password") != self.cleaned_data.get("password2"):
    #         # You cannot raise a ValidationError because you are not in the clean() method, so you need to add the error through the add_error method.
    #         self.add_error("password2", ValidationError('passwords are not the same', 'passwd_mismatch'))
    #         # You could also use None instead of "password2" if you do not want the error message to be linked to the field.
    #         if not self.errors:
    #             return True
    #     return False