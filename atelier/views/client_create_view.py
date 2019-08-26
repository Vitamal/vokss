from django.shortcuts import get_object_or_404, render
from atelier.models import Client
from django.views import generic

class ClientCreateView(generic.CreateView):
    model = Client
    fields = ('first_name', 'last_name', 'tel_number', 'place')
    template_name = 'atelier/client_form.html'
