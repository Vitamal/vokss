from django.utils.translation import gettext_lazy as _
from atelier.models import Client, Order
from atelier.forms import ClientForm
from django.urls import reverse_lazy
from atelier.views.base_view import AtelierFilterObjectsPreMixin, BaseListView, TailorPermissionPreMixin, \
    BaseDetailView, BaseUpdateView, BaseCreateView, BaseDeleteView


class ClientListView(AtelierFilterObjectsPreMixin, BaseListView):
    model = Client


class ClientCreateView(TailorPermissionPreMixin, BaseCreateView):
    model = Client
    form_class = ClientForm
    template_name = 'atelier/create_form.html'
    initial = {'place': _('Morshyn'), }


class ClientUpdateView(TailorPermissionPreMixin, AtelierFilterObjectsPreMixin, BaseUpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'atelier/create_form.html'


class ClientDetailView(AtelierFilterObjectsPreMixin, BaseDetailView):
    model = Client

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the orders
        context['order_list'] = Order.objects.all().filter(client=self.object)
        return context


class ClientDeleteView(TailorPermissionPreMixin, AtelierFilterObjectsPreMixin, BaseDeleteView):
    model = Client
    success_url = reverse_lazy('atelier:client_list')
    template_name = 'atelier/delete_form.html'
