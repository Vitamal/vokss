from django.shortcuts import get_object_or_404, render
from atelier.models import Product
from django.views import generic


class ProductDetailView(generic.DetailView):
    model = Product

