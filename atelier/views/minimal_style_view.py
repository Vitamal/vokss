from django.shortcuts import get_object_or_404, render
from atelier.models import MinimalStyle
from django.views import generic
from atelier.forms import MinimalStyleForm
from django.urls import reverse_lazy


class MinimalStyleDetailView(generic.DetailView):
    model = MinimalStyle
    fields = '__all__'
    template_name = 'atelier/minimal_style_detail.html'


class MinimalStyleListView(generic.ListView):
    model = MinimalStyle
    paginate_by = 10  # number of records on the one page
    template_name = 'atelier/minimal_style_list.html'


class MinimalStyleCreateView(generic.CreateView):
    model = MinimalStyle
    fields = '__all__'
    template_name = 'atelier/create_form.html'


class MinimalStyleUpdateView(generic.UpdateView):
    model = MinimalStyle
    form_class = MinimalStyleForm
    template_name = 'atelier/create_form.html'


class MinimalStyleDeleteView(generic.DeleteView):
    model = MinimalStyle
    success_url = reverse_lazy('atelier:minimal_style_list')
    template_name = 'atelier/delete_form.html'
