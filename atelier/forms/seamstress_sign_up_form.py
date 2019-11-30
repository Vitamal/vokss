from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from atelier.models import Profile


class SeamstressSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Profile

    def save(self, commit=True):
        user = super().save(commit=False)
        user.profile.is_seamstress = True
        if commit:
            user.save()
        return user
