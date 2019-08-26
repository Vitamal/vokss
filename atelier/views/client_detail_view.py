from atelier.models import Client, Order
from django.views import generic


class ClientDetailView(generic.DetailView):
    model = Client

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the orders
        context['order_list'] = Order.objects.all().filter(client=self.object)
        return context
