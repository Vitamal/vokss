from atelier.models import Profile
from django.views import generic
from atelier.forms import ProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile
    fields = '__all__'


class ProfileListView(LoginRequiredMixin, generic.ListView):
    model = Profile
    paginate_by = 10  # number of records on the one page


class ProfileCreateView(LoginRequiredMixin, generic.CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'atelier/create_form.html'


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'atelier/create_form.html'


class ProfileDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Profile
    success_url = reverse_lazy('atelier:profile_list')
    template_name = 'atelier/delete_form.html'
