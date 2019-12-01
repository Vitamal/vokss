from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from atelier.models import Profile
from atelier.forms import TailorSignUpForm


class TailorSignUpView(CreateView):
    model = Profile
    form_class = TailorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'tailor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('atelier:profile_list')
