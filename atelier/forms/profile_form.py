from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from atelier.models import Atelier


class ProfileRegisterForm(UserCreationForm):
    email = forms.EmailField()
    is_tailor = forms.BooleanField(label=_('Is Tailor'), required=False)

    def get_atelier(self):
        return self.request.user.profil.atelier

    atelier = forms.ModelChoiceField(queryset=Atelier.objects.filter(name=get_atelier()), disabled=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError(_('Email Already Exists'))
        return email


class ProfileChangeForm(UserChangeForm):
    email = forms.EmailField()
    is_tailor = forms.BooleanField(label=_('Is Tailor'), required=False)

    # rewrite this for add the link in help_text
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "!Raw passwords are not stored, so there is no way to see this "
            "user's password, but you can change the password using "
            "<a href=/accounts/password_change/?next=/en/atelier/profile/{}/edit/>this form</a>."
        ),
    )

    class Meta(ProfileRegisterForm.Meta):
        fields = ('email', 'is_tailor')
