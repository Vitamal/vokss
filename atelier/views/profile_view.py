from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.contrib import messages
from django.views.generic import FormView

from atelier.models import Profile
from django.views import generic
from atelier.forms import UserForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


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


class RegisterProfileView(FormView):
    template_name = 'atelier/profile_form.html'
    form_class = UserForm

    def get_success_url(self):
        return '/atelier/'

    def form_valid(self, form):
        print(form.__dict__)
        user = User.objects.create(
            email=form.fields.get('email'),
            username=form.fields.get('username'),
        )
        user.set_password(form.password)
        Profile.objects.create(
            user=user,
            atelier=self.request.user.profile.atelier,
            is_tailor=form.fields.get('is_tailor'),
        )
        return super().form_valid(form)


class ProfileDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Profile
    success_url = reverse_lazy('atelier:profile_list')
    template_name = 'atelier/delete_form.html'
