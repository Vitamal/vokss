from atelier.models import Tailor
from django.views import generic
from atelier.forms import TailorForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class TailorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tailor
    fields = '__all__'


class TailorListView(LoginRequiredMixin, generic.ListView):
    model = Tailor
    paginate_by = 10  # number of records on the one page


class TailorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tailor
    form_class = TailorForm
    template_name = 'atelier/create_form.html'


class TailorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tailor
    form_class = TailorForm
    template_name = 'atelier/create_form.html'


class TailorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tailor
    success_url = reverse_lazy('atelier:tailor_list')
    template_name = 'atelier/delete_form.html'
