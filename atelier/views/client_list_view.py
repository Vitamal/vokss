from django.shortcuts import get_object_or_404, render
from atelier.models import Client
from django.views import generic


class ClientListView(generic.ListView):
    model = Client
    paginate_by = 10  # number of records on the one page
