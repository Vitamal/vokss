from atelier.models import Product
from atelier.forms import ProductForm
from django.urls import reverse_lazy
from atelier.views.base_view import AtelierFilterObjectsPreMixin, BaseListView, TailorPermissionPreMixin, \
    BaseDetailView, BaseDeleteView, BaseUpdateView, BaseCreateView


class ProductDetailView(AtelierFilterObjectsPreMixin, BaseDetailView):
    model = Product
    fields = '__all__'


class ProductListView(AtelierFilterObjectsPreMixin, BaseListView):
    model = Product


class ProductCreateView(TailorPermissionPreMixin, BaseCreateView):
    model = Product
    form_class = ProductForm
    template_name = 'atelier/create_form.html'


class ProductUpdateView(TailorPermissionPreMixin, AtelierFilterObjectsPreMixin, BaseUpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'atelier/create_form.html'


class ProductDeleteView(TailorPermissionPreMixin, AtelierFilterObjectsPreMixin, BaseDeleteView):
    model = Product
    success_url = reverse_lazy('atelier:product_list')
    template_name = 'atelier/delete_form.html'
