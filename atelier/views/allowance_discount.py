from django.shortcuts import get_object_or_404, render
from atelier.models import AllowanceDiscount
from django.views import generic
from atelier.forms import AllowanceDiscountForm
from django.urls import reverse_lazy



class AllowanceDiscountDetailView(generic.DetailView):
    model = AllowanceDiscount
    fields = '__all__'

class AllowanceDiscountListView(generic.ListView):
    model = AllowanceDiscount
    paginate_by = 10  # number of records on the one page

class AllowanceDiscountCreateView(generic.CreateView):
    model = AllowanceDiscount
    fields = '__all__'
    template_name = 'atelier/allowance_aiscount_form.html'

class AllowanceDiscountUpdateView(generic.UpdateView):
    model = AllowanceDiscount
    form_class = AllowanceDiscountForm
    template_name = 'atelier/allowance_aiscount_update_form.html'


class AllowanceDiscountDeleteView(generic.DeleteView):
    model = AllowanceDiscount
    success_url = reverse_lazy('atelier:allowance_discount_list')
