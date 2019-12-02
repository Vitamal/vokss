from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from atelier.models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('atelier', 'is_tailor')


class SignUpForm(UserCreationForm):
    atelier = forms.ModelChoiceField(queryset=None, help_text='Atelier for the user is active now')
    is_tailor = forms.BooleanField(required=False, help_text='The tailor user has admin permissions for the atelier')

    '''
    Set the atelier field of new Profile equal to atelier of creator user
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = User.objects.filter(is_active=True)
        self.fields['atelier'].queryset = user.profile.atelier

    class Meta:
        model = User
        fields = ('username', 'is_tailor', 'password1', 'password2', )
