from atelier.app_utils import order_price_calculation
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

    # def get_order_price(self):
    #     order = self.object
    #     complication_elements_list = []
    #     for i in order.complication_elements.all():
    #         complication_elements_list.append(i.base_price)
    #     return order_price_calculation(complication_elements_list)
    #
    #
    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     print(context_data)
    #     context_data['test_context_data'] = self.get_order_price()
    #     return context_data



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

