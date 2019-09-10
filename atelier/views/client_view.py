from django.utils.translation import gettext_lazy as _

from atelier.models import Client, Order
from django.views import generic
from atelier.forms import ClientForm
from django.urls import reverse_lazy


class ClientCreateView(generic.CreateView):
    model = Client
    fields = ('first_name', 'last_name', 'tel_number', 'place')
    template_name = 'atelier/create_form.html'
    initial = {'place': _('Morshyn'), }


class ClientUpdateView(generic.UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'atelier/create_form.html'


class ClientListView(generic.ListView):
    model = Client
    paginate_by = 10  # number of records on the one page


class ClientDetailView(generic.DetailView):
    model = Client

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the orders
        context['order_list'] = Order.objects.all().filter(client=self.object)
        return context


class ClientDeleteView(generic.DeleteView):
    model = Client
    success_url = reverse_lazy('atelier:client_list')
    template_name = 'atelier/delete_form.html'
