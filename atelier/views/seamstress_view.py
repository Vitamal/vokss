from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from atelier.forms import SeamstressSignUpForm
from atelier.models import Profile


class SeamstressSignUpView(CreateView):
    model = Profile
    form_class = SeamstressSignUpForm
    template_name = 'registration/../templates/atelier/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'seamstress'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('atelier:home')
