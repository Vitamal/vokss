from atelier.models import Fabric
from django.views import generic
from atelier.forms import FabricForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class FabricDetailView(LoginRequiredMixin, generic.DetailView):
    model = Fabric
    fields = '__all__'

class FabricListView(LoginRequiredMixin, generic.ListView):
    model = Fabric
    paginate_by = 10  # number of records on the one page

class FabricCreateView(LoginRequiredMixin, generic.CreateView):
    model = Fabric
    form_class = FabricForm
    template_name = 'atelier/create_form.html'

class FabricUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Fabric
    form_class = FabricForm
    template_name = 'atelier/create_form.html'


class FabricDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Fabric
    success_url = reverse_lazy('atelier:fabric_list')
    template_name = 'atelier/delete_form.html'

