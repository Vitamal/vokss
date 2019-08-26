from django.shortcuts import get_object_or_404, render
from atelier.models import Client
from django.views import generic
from atelier.forms import ClientForm


class ClientUpdateView(generic.UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'atelier/client_update_form.html'