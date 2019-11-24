from atelier.models import Atelier
from django.views import generic
from atelier.forms import AtelierForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class AtelierDetailView(LoginRequiredMixin, generic.DetailView):
    model = Atelier
    fields = '__all__'


class AtelierListView(LoginRequiredMixin, generic.ListView):
    model = Atelier
    paginate_by = 10  # number of records on the one page


class AtelierCreateView(LoginRequiredMixin, generic.CreateView):
    model = Atelier
    form_class = AtelierForm
    template_name = 'atelier/create_form.html'


class AtelierUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Atelier
    form_class = AtelierForm
    template_name = 'atelier/create_form.html'


class AtelierDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Atelier
    success_url = reverse_lazy('atelier:atelier_list')
    template_name = 'atelier/delete_form.html'
