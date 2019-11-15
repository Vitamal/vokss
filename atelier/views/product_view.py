from atelier.models import Product
from django.views import generic
from atelier.forms import ProductForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    model = Product
    fields = '__all__'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Product.objects.all()  # admin user access all orders
        else:
            return Product.objects.filter(
                tailor__username=self.request.user)  # ordinary user access his own orders only


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product
    paginate_by = 10  # number of records on the one page

    def get_queryset(self):
        if self.request.user.is_staff:
            return Product.objects.all()  # admin user access all orders
        else:
            return Product.objects.filter(
                tailor__username=self.request.user)  # ordinary user access his own orders only


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'atelier/create_form.html'

    def form_valid(self, form):
        self.object = form.save()
        self.object.update(tailor=self.request.user)
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'atelier/create_form.html'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Product.objects.all()  # admin user access all orders
        else:
            return Product.objects.filter(
                tailor__username=self.request.user)  # ordinary user access his own orders only


class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy('atelier:product_list')
    template_name = 'atelier/delete_form.html'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Product.objects.all()  # admin user access all orders
        else:
            return Product.objects.filter(
                tailor__username=self.request.user)  # ordinary user access his own orders only
