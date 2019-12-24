from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class ProfileRegisterForm(UserCreationForm):
    email = forms.EmailField()
    is_tailor = forms.BooleanField(required=False)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError(_('Email Already Exists'))
        return email


class ProfileChangeForm(forms.Form):
    email = forms.EmailField()
    is_tailor = forms.BooleanField(required=False)
