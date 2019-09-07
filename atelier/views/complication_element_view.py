from atelier.models import ComplicationElement
from django.views import generic
from atelier.forms import ComplicationElementForm
from django.urls import reverse_lazy



class ComplicationElementDetailView(generic.DetailView):
    model = ComplicationElement
    fields = '__all__'
    template_name = 'atelier/complication_element_detail.html'


class ComplicationElementListView(generic.ListView):
    model = ComplicationElement
    paginate_by = 10  # number of records on the one page
    template_name = 'atelier/complication_element_list.html'

class ComplicationElementCreateView(generic.CreateView):
    model = ComplicationElement
    fields = '__all__'
    template_name = 'atelier/create_form.html'

class ComplicationElementUpdateView(generic.UpdateView):
    model = ComplicationElement
    form_class = ComplicationElementForm
    template_name = 'atelier/create_form.html'


class ComplicationElementDeleteView(generic.DeleteView):
    model = ComplicationElement
    success_url = reverse_lazy('atelier:complication_element_list')
    template_name = 'atelier/delete_form.html'
