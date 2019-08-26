from django.shortcuts import get_object_or_404, render
from atelier.models import Order
from django.views import generic


class OrderListView(generic.ListView):
    model = Order
    paginate_by = 10  # number of records on the one page
