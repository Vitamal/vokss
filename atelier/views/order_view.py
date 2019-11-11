from atelier.app_utils import order_price_calculation
from atelier.forms import OrderForm
from atelier.models import Order
from django.views import generic
from django.urls import reverse_lazy



class OrderCreateView(generic.CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'atelier/order_form.html'


class OrderDetailView(generic.DetailView):
    model = Order
    fields = '__all__'

    def get_order_price(self):
        order = self.object
        complication_elements_base_price_list = []
        complication_elements_complexity_list = []
        allowance_discount_coefficient_list = []

        for i in order.complication_elements.all():
            complication_elements_base_price_list.append(i.base_price)

        for j in order.complication_elements.all():
            complication_elements_complexity_list.append(j.complexity)

        for k in order.allowance_discount.all():
            allowance_discount_coefficient_list.append(k.coefficient)

        return order_price_calculation(order.fabric.complexity_factor, order.product.base_price,
                                       complication_elements_base_price_list, complication_elements_complexity_list,
                                       order.processing_category, allowance_discount_coefficient_list)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        print(context_data)
        context_data['order_price_view'] = self.get_order_price()
        return context_data


class OrderListView(generic.ListView):
    model = Order
    paginate_by = 10  # number of records on the one page


class OrderUpdateView(generic.UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'atelier/order_form.html'


class OrderDeleteView(generic.DeleteView):
    model = Order
    success_url = reverse_lazy('atelier:client_list')
    template_name = 'atelier/delete_form.html'


