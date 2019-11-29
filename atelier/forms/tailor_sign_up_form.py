from django.contrib.auth.forms import UserCreationForm
from atelier.models import Profile


class TailorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Profile

    def save(self, commit=True):
        user = super().save(commit=False)
        user.profile.is_tailor = True
        if commit:
            user.save()
        return user
