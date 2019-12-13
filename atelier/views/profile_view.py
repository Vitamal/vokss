from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render_to_response, redirect
from django.contrib import messages
from django.views.generic import FormView
import django.core.validators
from atelier.models import Profile
from django.views import generic
from atelier.forms import UserForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView
from django.contrib import messages


class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile
    fields = '__all__'


class ProfileListView(LoginRequiredMixin, generic.ListView):
    model = Profile
    paginate_by = 10  # number of records on the one page


# def register(request):
#     if request.method == 'POST':
#         form = UserForm(data=request.POST)
#         print(form.__dict__)
#         if form.is_valid():
#             user = form.save()
#             pw = user.password
#             user.set_password(pw)
#             user.save()
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = UserForm()
#     return render_to_response('atelier/profile_form.html', {'form': form})

class ProfileCreateView(UserPassesTestMixin, FormView):

    def test_func(self):
        # tailor only can create new users in the own atelier
        return self.request.user.profile.is_tailor

    template_name = 'atelier/create_form.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse_lazy('atelier:profile_list')


    def form_valid(self, form):  # The default implementation for form_valid() simply redirects to the success_url.
        print(form.__dict__)
        user = User.objects.create(
            email=form.cleaned_data['email'],
            username=form.cleaned_data['username'],
        )
        user.set_password(form.cleaned_data['password'])
        user.save()
        Profile.objects.create(
            user=user,
            atelier=self.request.user.profile.atelier,
            is_tailor=form.cleaned_data['is_tailor'],
            created_by=self.request.user,
            last_updated_by=self.request.user,
        )
        return super().form_valid(form)


class ProfileDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Profile
    success_url = reverse_lazy('atelier:profile_list')
    template_name = 'atelier/delete_form.html'
