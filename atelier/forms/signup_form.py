from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    atelier = forms.CharField(max_length=100, help_text='Atelier')
    is_tailor = forms.BooleanField(required=False, help_text='Tailor')
    is_seamstress = forms.BooleanField(required=False, help_text='Seamstress')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'atelier',
                  'password1', 'is_tailor', 'is_seamstress', 'password2',)
