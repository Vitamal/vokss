from atelier.models import Fabric
from atelier.forms import FabricForm
from django.urls import reverse_lazy
from atelier.views.base_view import BaseDetailView, BaseListView, \
    SuperuserPermissionPreMixin, BaseCreateView, BaseUpdateView, BaseDeleteView


class FabricDetailView(BaseDetailView):
    model = Fabric
    fields = '__all__'


class FabricListView(BaseListView):
    model = Fabric


class FabricCreateView(SuperuserPermissionPreMixin, BaseCreateView):
    model = Fabric
    form_class = FabricForm
    template_name = 'atelier/create_form.html'


class FabricUpdateView(SuperuserPermissionPreMixin, BaseUpdateView):
    model = Fabric
    form_class = FabricForm
    template_name = 'atelier/create_form.html'


class FabricDeleteView(SuperuserPermissionPreMixin, BaseDeleteView):
    model = Fabric
    success_url = reverse_lazy('atelier:fabric_list')
    template_name = 'atelier/delete_form.html'
