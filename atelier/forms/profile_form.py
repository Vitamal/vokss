from django import forms


class UserForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(max_length=50)
    password2 = forms.CharField(max_length=50)
    is_tailor = forms.BooleanField()
