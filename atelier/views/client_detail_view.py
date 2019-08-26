from atelier.models import Client
from django.views import generic


class ClientDetailView(generic.DetailView):
    model = Client
