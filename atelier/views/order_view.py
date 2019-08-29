from atelier.models import Order
from django.views import generic


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

