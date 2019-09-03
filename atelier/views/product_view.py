from atelier.models import Product
from django.views import generic
from atelier.forms import ProductForm
from django.urls import reverse_lazy



class ProductDetailView(generic.DetailView):
    model = Product
    fields = '__all__'


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 10  # number of records on the one page

class ProductCreateView(generic.CreateView):
    model = Product
    fields = '__all__'
    template_name = 'atelier/create_form.html'

class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'atelier/create_form.html'


class ProductDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('atelier:product_list')
    template_name = 'atelier/delete_form.html'
