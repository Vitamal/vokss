from atelier.models import Product
from django.views import generic
from atelier.forms import ProductForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    model = Product
    fields = '__all__'


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product
    paginate_by = 10  # number of records on the one page

class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'atelier/create_form.html'

class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'atelier/create_form.html'


class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy('atelier:product_list')
    template_name = 'atelier/delete_form.html'
