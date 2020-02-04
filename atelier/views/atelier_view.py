from atelier.models import Atelier, Profile
from atelier.forms import AtelierForm
from django.urls import reverse_lazy
from atelier.views.base_view import BaseDetailView, BaseListView, \
    SuperuserPermissionPreMixin, BaseCreateView, BaseUpdateView, BaseDeleteView


class AtelierDetailView(SuperuserPermissionPreMixin, BaseDetailView):
    model = Atelier
    fields = '__all__'


class AtelierListView(SuperuserPermissionPreMixin, BaseListView):
    model = Atelier


    # def get_context_data(self, *, object_list=None, **kwargs):
    #     num_tailors = Profile.objects.filter(is_tailor=True).count()
    #     num_simple_users = Profile.objects.filter(is_tailor=False).count()
    #     context = {
    #         'num_tailors': num_tailors,
    #         'num_simple_users': num_simple_users,
    #     }
    #     return super().get_context_data(**context)


class AtelierCreateView(SuperuserPermissionPreMixin, BaseCreateView):
    model = Atelier
    form_class = AtelierForm
    template_name = 'atelier/create_form.html'


class AtelierUpdateView(SuperuserPermissionPreMixin, BaseUpdateView):
    model = Atelier
    form_class = AtelierForm
    template_name = 'atelier/create_form.html'


class AtelierDeleteView(SuperuserPermissionPreMixin, BaseDeleteView):
    model = Atelier
    success_url = reverse_lazy('atelier:atelier_list')
    template_name = 'atelier/delete_form.html'
