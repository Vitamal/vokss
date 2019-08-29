from atelier.forms import OrderForm
from atelier.models import Order
from django.views import generic
from django.urls import reverse_lazy



class OrderCreateView(generic.CreateView):
    model = Order
    fields = '__all__'
    template_name = 'atelier/order_form.html'


class OrderDetailView(generic.DetailView):
    model = Order
    fields = '__all__'


class OrderListView(generic.ListView):
    model = Order
    paginate_by = 10  # number of records on the one page


class OrderUpdateView(generic.UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'atelier/order_update_form.html'


class OrderDeleteView(generic.DeleteView):
    model = Order
    success_url = reverse_lazy('atelier:client_list')
