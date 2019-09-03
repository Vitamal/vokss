from django.shortcuts import get_object_or_404, render
from atelier.models import Fabric
from django.views import generic
from atelier.forms import FabricForm
from django.urls import reverse_lazy



class FabricDetailView(generic.DetailView):
    model = Fabric
    fields = '__all__'

class FabricListView(generic.ListView):
    model = Fabric
    paginate_by = 10  # number of records on the one page

class FabricCreateView(generic.CreateView):
    model = Fabric
    fields = '__all__'
    template_name = 'atelier/create_form.html'

class FabricUpdateView(generic.UpdateView):
    model = Fabric
    form_class = FabricForm
    template_name = 'atelier/create_form.html'


class FabricDeleteView(generic.DeleteView):
    model = Fabric
    success_url = reverse_lazy('atelier:fabric_list')
