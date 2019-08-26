from django.shortcuts import get_object_or_404, render
from atelier.models import Product
from django.views import generic


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 10  # number of records on the one page

