from atelier.models import AllowanceDiscount
from django.views import generic
from atelier.forms import AllowanceDiscountForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class AllowanceDiscountDetailView(LoginRequiredMixin, generic.DetailView):
    model = AllowanceDiscount
    fields = '__all__'
    template_name = 'atelier/allowance_discount_detail.html'
    context_object_name = 'allowance_discount'  # we changed lowercased version of the model class’ name:
                                                # allowancediscount to allowance_discount.


class AllowanceDiscountListView(LoginRequiredMixin, generic.ListView):
    model = AllowanceDiscount
    paginate_by = 10  # number of records on the one page
    template_name = 'atelier/allowance_discount_list.html'
    context_object_name = 'allowance_discount_list'


class AllowanceDiscountCreateView(LoginRequiredMixin, generic.CreateView):
    model = AllowanceDiscount
    form_class = AllowanceDiscountForm
    template_name = 'atelier/create_form.html'


class AllowanceDiscountUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = AllowanceDiscount
    form_class = AllowanceDiscountForm
    template_name = 'atelier/create_form.html'


class AllowanceDiscountDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = AllowanceDiscount
    success_url = reverse_lazy('atelier:allowance_discount_list')
    template_name = 'atelier/delete_form.html'
