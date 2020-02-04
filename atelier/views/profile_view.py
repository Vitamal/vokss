from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from atelier.models import Profile
from django.views import generic
from atelier.forms import ProfileRegisterForm, ProfileChangeForm
from django.urls import reverse_lazy
from atelier.views.base_view import AtelierFilterObjectsPreMixin, BaseListView, TailorPermissionPreMixin, \
    BaseDetailView, BaseDeleteView, BaseUpdateView


class ProfileDetailView(TailorPermissionPreMixin, AtelierFilterObjectsPreMixin, BaseDetailView):
    model = Profile
    fields = '__all__'


class ProfileListView(AtelierFilterObjectsPreMixin, TailorPermissionPreMixin, BaseListView):
    model = Profile


class ProfileCreateView(TailorPermissionPreMixin, FormView):
    template_name = 'atelier/create_form.html'
    form_class = ProfileRegisterForm

    def get_initial(self):
        """
        Returns the initial data to use for atelier form field.
        """
        initial = super().get_initial()
        initial['atelier'] = self.request.user.profile.atelier
        return initial

    def get_success_url(self):
        return reverse_lazy('atelier:profile_list')

    def form_valid(self, form):
        # The default implementation for form_valid() simply redirects to the success_url.
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


class ProfileChangeView(AtelierFilterObjectsPreMixin, TailorPermissionPreMixin, BaseUpdateView):
    model = Profile
    template_name = 'atelier/create_form.html'
    form_class = ProfileChangeForm

    def get_success_url(self):
        return reverse_lazy('atelier:profile_list')

    def get_profile_object(self):
        profile_id = self.kwargs.get('pk')
        return Profile.objects.get(id=profile_id)

    def get_initial(self):
        data = {
            'email': self.get_profile_object().user.email,
            'is_tailor': self.get_profile_object().is_tailor
        }
        return data

    def form_valid(self, form):
        # The default implementation for form_valid() simply redirects to the success_url.
        profile = self.get_profile_object()
        profile.is_tailor = form.cleaned_data['is_tailor']
        profile.user.email = form.cleaned_data['email']
        profile.last_updated_by = self.request.user
        profile.full_clean()
        profile.save()
        profile.user.save()
        return super().form_valid(form)


class ProfileDeleteView(TailorPermissionPreMixin, AtelierFilterObjectsPreMixin, BaseDeleteView):
    model = Profile
    success_url = reverse_lazy('atelier:profile_list')
    template_name = 'atelier/delete_form.html'

    def get_user_object(self):
        profile_id = self.kwargs.get('pk')
        profile = Profile.objects.get(pk=profile_id)
        return profile.user

    def delete(self, request, *args, **kwargs):
        """
        Overriding the delete() method to delete User instances, and according Profile instance will be deleted too.
        """
        self.object = self.get_user_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse_lazy('atelier:profile_list')
