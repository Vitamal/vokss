from urllib import request

from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic import FormView, UpdateView
from atelier.models import Profile
from django.views import generic
from atelier.forms import ProfileRegisterForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile
    fields = '__all__'


class ProfileListView(LoginRequiredMixin, generic.ListView):
    model = Profile
    paginate_by = 10  # number of records on the one page


class ProfileCreateView(UserPassesTestMixin, FormView):

    def test_func(self):
        # tailor only can create new users in the own atelier
        return self.request.user.profile.is_tailor

    template_name = 'atelier/create_form.html'
    form_class = ProfileRegisterForm

    def get_success_url(self):
        return reverse_lazy('atelier:profile_list')

    def form_valid(self, form):  # The default implementation for form_valid() simply redirects to the success_url.
        user = User.objects.create(
            email=form.cleaned_data['email'],
            username=form.cleaned_data['username'],
        )
        user.set_password(form.cleaned_data['password2'])
        user.save()
        Profile.objects.create(
            user=user,
            atelier=self.request.user.profile.atelier,
            is_tailor=form.cleaned_data['is_tailor'],
            created_by=self.request.user,
            last_updated_by=self.request.user,
        )
        return super().form_valid(form)


class ProfileChangeView(UserPassesTestMixin, UpdateView):

    def test_func(self):
        # tailor only can create new users in the own atelier
        return self.request.user.profile.is_tailor

    template_name = 'atelier/create_form.html'
    form_class = ProfileRegisterForm

    def get_object(self, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        email = user.email

        # We can also get user object using self.request.user  but that doesnt work
        # for other models.

        return user

    def form_valid(self, form):  # The default implementation for form_valid() simply redirects to the success_url.
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('atelier:profile_list')

def change_profile(request):
    if request.method == 'POST':
        form = ProfileRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            # pw = user.password
            # user.set_password(pw)
            # user.save()
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProfileRegisterForm()
    return render_to_response('atelier/create_form.html', {'form': form})


class ProfileDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Profile
    success_url = reverse_lazy('atelier:profile_list')
    template_name = 'atelier/delete_form.html'
