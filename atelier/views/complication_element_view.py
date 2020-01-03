from atelier.models import ComplicationElement
from atelier.forms import ComplicationElementForm
from django.urls import reverse_lazy
from atelier.views.base_view import BaseDetailView, BaseListView, SuperuserCreateView, SuperuserUpdateView, \
         SuperuserDeleteView


class ComplicationElementDetailView(BaseDetailView):
    model = ComplicationElement
    fields = '__all__'
    template_name = 'atelier/complication_element_detail.html'


class ComplicationElementListView(BaseListView):
    model = ComplicationElement
    template_name = 'atelier/complication_element_list.html'


class ComplicationElementCreateView(SuperuserCreateView):
    model = ComplicationElement
    form_class = ComplicationElementForm
    template_name = 'atelier/create_form.html'


class ComplicationElementUpdateView(SuperuserUpdateView):
    model = ComplicationElement
    form_class = ComplicationElementForm
    template_name = 'atelier/create_form.html'


class ComplicationElementDeleteView(SuperuserDeleteView):
    model = ComplicationElement
    success_url = reverse_lazy('atelier:complication_element_list')
    template_name = 'atelier/delete_form.html'
