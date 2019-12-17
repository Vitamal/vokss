from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from atelier.models import Profile


class ProfileRegisterForm(UserCreationForm):
    email = forms.EmailField()
    is_tailor = forms.BooleanField(required=False)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email Already Exists')
        return email


class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ('user', 'is_tailor')
    # email = forms.EmailField()
    # is_tailor = forms.BooleanField(required=False)
    # exclude = ('groups',)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email Already Exists')
        return email
