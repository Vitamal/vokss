from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from atelier.models import Profile


class TailorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_tailor = True
        if commit:
            user.save()
        return user
