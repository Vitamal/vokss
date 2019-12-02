from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render
from django.contrib import messages

from atelier.models import Profile
from django.views import generic
from atelier.forms import ProfileForm, UserForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile
    fields = '__all__'


class ProfileListView(LoginRequiredMixin, generic.ListView):
    model = Profile
    paginate_by = 10  # number of records on the one page

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'atelier/profile_form.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

# class ProfileCreateView(LoginRequiredMixin, generic.CreateView):
#     model = Profile
#     form_class = ProfileForm
#     template_name = 'atelier/create_form.html'
#
#
# class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
#     model = Profile
#     form_class = ProfileForm
#     template_name = 'atelier/create_form.html'


class ProfileDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Profile
    success_url = reverse_lazy('atelier:profile_list')
    template_name = 'atelier/delete_form.html'
