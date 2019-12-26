from atelier.models import MinimalStyle
from atelier.forms import MinimalStyleForm
from django.urls import reverse_lazy
from atelier.views.base_view import BaseDetailView, BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView

class MinimalStyleDetailView(BaseDetailView):
    model = MinimalStyle
    fields = '__all__'
    template_name = 'atelier/minimal_style_detail.html'


class MinimalStyleListView(BaseListView):
    model = MinimalStyle
    template_name = 'atelier/minimal_style_list.html'


class MinimalStyleCreateView(BaseCreateView):
    model = MinimalStyle
    form_class = MinimalStyleForm
    template_name = 'atelier/create_form.html'


class MinimalStyleUpdateView(BaseUpdateView):
    model = MinimalStyle
    form_class = MinimalStyleForm
    template_name = 'atelier/create_form.html'


class MinimalStyleDeleteView(BaseDeleteView):
    model = MinimalStyle
    success_url = reverse_lazy('atelier:minimal_style_list')
    template_name = 'atelier/delete_form.html'
