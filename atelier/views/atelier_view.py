from atelier.models import Atelier
from atelier.forms import AtelierForm
from django.urls import reverse_lazy
from atelier.views.base_view import BaseDetailView, BaseListView, SuperuserCreateView, SuperuserUpdateView, \
        SuperuserPermissionPreMixin, SuperuserDeleteView


class AtelierDetailView(SuperuserPermissionPreMixin, BaseDetailView):
    model = Atelier
    fields = '__all__'


class AtelierListView(SuperuserPermissionPreMixin, BaseListView):
    model = Atelier


class AtelierCreateView(SuperuserCreateView):
    model = Atelier
    form_class = AtelierForm
    template_name = 'atelier/create_form.html'


class AtelierUpdateView(SuperuserUpdateView):
    model = Atelier
    form_class = AtelierForm
    template_name = 'atelier/create_form.html'


class AtelierDeleteView(SuperuserDeleteView):
    model = Atelier
    success_url = reverse_lazy('atelier:atelier_list')
    template_name = 'atelier/delete_form.html'
