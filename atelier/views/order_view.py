from atelier.app_utils import order_price_calculation
from atelier.forms import OrderForm
from atelier.models import Order
from django.views import generic
from django.urls import reverse_lazy

from atelier.views import BaseListView, TailorPermissionPreMixin, AtelierFilterObjectsPreMixin, BaseDetailView, \
    BaseCreateView, BaseUpdateView, BaseDeleteView


class OrderCreateView(TailorPermissionPreMixin, BaseCreateView):
    model = Order
    form_class = OrderForm
    template_name = 'atelier/order_form.html'

    def form_valid(self, form):
        # assign base attributes to order instance
        atelier = self.request.user.profile.atelier
        created_by = self.request.user
        last_updated_by = self.request.user
        order = form.save()
        order.atelier = atelier
        order.created_by = created_by
        order.last_updated_by = last_updated_by
        order.save()
        return super().form_valid(form)


class OrderDetailView(AtelierFilterObjectsPreMixin, BaseDetailView):
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
        context_data['order_price_view'] = self.get_order_price()
        return context_data


class OrderUpdateView(TailorPermissionPreMixin, AtelierFilterObjectsPreMixin, BaseUpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'atelier/order_form.html'

    def form_valid(self, form):
        # assign last_updated_by attribute to order instance
        last_updated_by = self.request.user
        order = form.save()
        order.last_updated_by = last_updated_by
        order.save()
        return super().form_valid(form)


class OrderListView(AtelierFilterObjectsPreMixin, BaseListView):
    model = Order
    template_name = 'atelier/order_list.html'
    context_object_name = 'order_list'


class OrderDeleteView(TailorPermissionPreMixin, AtelierFilterObjectsPreMixin, BaseDeleteView):
    model = Order
    success_url = reverse_lazy('atelier:client_list')
    template_name = 'atelier/delete_form.html'
