from atelier.models import MinimalStyle
from django.views import generic
from atelier.forms import MinimalStyleForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class MinimalStyleDetailView(LoginRequiredMixin, generic.DetailView):
    model = MinimalStyle
    fields = '__all__'
    template_name = 'atelier/minimal_style_detail.html'


class MinimalStyleListView(LoginRequiredMixin, generic.ListView):
    model = MinimalStyle
    paginate_by = 10  # number of records on the one page
    template_name = 'atelier/minimal_style_list.html'


class MinimalStyleCreateView(LoginRequiredMixin, generic.CreateView):
    model = MinimalStyle
    form_class = MinimalStyleForm
    template_name = 'atelier/create_form.html'


class MinimalStyleUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = MinimalStyle
    form_class = MinimalStyleForm
    template_name = 'atelier/create_form.html'


class MinimalStyleDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = MinimalStyle
    success_url = reverse_lazy('atelier:minimal_style_list')
    template_name = 'atelier/delete_form.html'
