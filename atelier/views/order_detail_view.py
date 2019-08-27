from atelier.models import Order
from django.views import generic


class OrderDetailView(generic.DetailView):
    model = Order

