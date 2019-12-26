from atelier.models import Product
from django.views import generic
from atelier.forms import ProductForm
from django.urls import reverse_lazy
from atelier.views.base_view import AtelierFilterObjectsPreMixin, BaseListView, TailorPermissionPreMixin


class ProductDetailView(AtelierFilterObjectsPreMixin, generic.DetailView):
    model = Product
    fields = '__all__'


class ProductListView(AtelierFilterObjectsPreMixin, BaseListView):
    model = Product


class ProductCreateView(TailorPermissionPreMixin, generic.CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'atelier/create_form.html'


class ProductUpdateView(TailorPermissionPreMixin, AtelierFilterObjectsPreMixin, generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'atelier/create_form.html'


class ProductDeleteView(TailorPermissionPreMixin, AtelierFilterObjectsPreMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy('atelier:product_list')
    template_name = 'atelier/delete_form.html'
