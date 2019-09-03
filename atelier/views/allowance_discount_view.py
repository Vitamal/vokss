from atelier.models import AllowanceDiscount
from django.views import generic
from atelier.forms import AllowanceDiscountForm
from django.urls import reverse_lazy



class AllowanceDiscountDetailView(generic.DetailView):
    model = AllowanceDiscount
    fields = '__all__'
    template_name = 'atelier/allowance_discount_detail.html'


class AllowanceDiscountListView(generic.ListView):
    model = AllowanceDiscount
    paginate_by = 10  # number of records on the one page
    template_name = 'atelier/allowance_discount_list.html'


class AllowanceDiscountCreateView(generic.CreateView):
    model = AllowanceDiscount
    fields = '__all__'
    template_name = 'atelier/create_form.html'

class AllowanceDiscountUpdateView(generic.UpdateView):
    model = AllowanceDiscount
    form_class = AllowanceDiscountForm
    template_name = 'atelier/create_form.html'


class AllowanceDiscountDeleteView(generic.DeleteView):
    model = AllowanceDiscount
    success_url = reverse_lazy('atelier:allowance_discount_list')
    template_name = 'atelier/delete_form.html'
