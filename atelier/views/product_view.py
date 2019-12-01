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
            return Product.objects.all()  # admin user access all products
        else:
            return Product.objects.filter(
                atelier=self.request.user.profile.atelier)  # ordinary user access his atelier products only


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product
    paginate_by = 10  # number of records on the one page

    def get_queryset(self):
        if self.request.user.is_staff:
            return Product.objects.all()  # admin user access all products
        else:
            return Product.objects.filter(
                atelier=self.request.user.profile.atelier)  # ordinary user access his atelier products only


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'atelier/create_form.html'

    # def form_valid(self, form):
    #     self.object = form.save()
    #     atelier_id = self.kwargs.get('atelier_id')
    #     self.object.update(atelier_id=atelier_id)
    #     return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'atelier/create_form.html'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Product.objects.all()  # admin user access all products
        else:
            return Product.objects.filter(
                atelier=self.request.user.profile.atelier)  # ordinary user access his atelier products only


class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy('atelier:product_list')
    template_name = 'atelier/delete_form.html'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Product.objects.all()  # admin user access all products
        else:
            return Product.objects.filter(
                atelier=self.request.user.profile.atelier)  # ordinary user access his atelier products only
