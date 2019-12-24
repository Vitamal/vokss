from django.utils.decorators import method_decorator
from atelier.models import AllowanceDiscount
from django.views import generic
from atelier.forms import AllowanceDiscountForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test

from atelier.views.base_view import *


class AllowanceDiscountDetailView(BaseDetailView):
    model = AllowanceDiscount
    fields = '__all__'
    template_name = 'atelier/allowance_discount_detail.html'
    context_object_name = 'allowance_discount'  # we changed lowercased version of the model class’ name:
                                                # allowancediscount to allowance_discount.


class AllowanceDiscountListView(BaseListView):
    model = AllowanceDiscount
    paginate_by = 10  # number of records on the one page
    template_name = 'atelier/allowance_discount_list.html'
    context_object_name = 'allowance_discount_list'


class AllowanceDiscountCreateView(UserPassesTestMixin, generic.CreateView):
    permission_required = 'is_staff'
    model = AllowanceDiscount
    form_class = AllowanceDiscountForm
    template_name = 'atelier/create_form.html'

    """
    check permissions in class-based views with the help of UserPassesTestMixin and test_funk
    """

    def test_func(self):
        return self.request.user.is_superuser


class AllowanceDiscountUpdateView(UserPassesTestMixin, generic.UpdateView):
    model = AllowanceDiscount
    form_class = AllowanceDiscountForm
    template_name = 'atelier/create_form.html'

    """
    check permissions in class-based views with the help of UserPassesTestMixin and test_funk
    """

    def test_func(self):
        return self.request.user.is_superuser


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class AllowanceDiscountDeleteView(LoginRequiredMixin, generic.DeleteView):
    redirect_field_name = 'redirect_to'
    model = AllowanceDiscount
    success_url = reverse_lazy('atelier:allowance_discount_list')
    template_name = 'atelier/delete_form.html'
