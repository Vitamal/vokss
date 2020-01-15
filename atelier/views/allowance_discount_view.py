from atelier.models import AllowanceDiscount
from atelier.forms import AllowanceDiscountForm
from django.urls import reverse_lazy
from atelier.views.base_view import BaseDetailView, BaseListView, \
    SuperuserPermissionPreMixin, BaseCreateView, BaseUpdateView, BaseDeleteView


class AllowanceDiscountDetailView(BaseDetailView):
    model = AllowanceDiscount
    fields = '__all__'
    template_name = 'atelier/allowance_discount_detail.html'
    # we changed lowercase version of the model class’ name:
    # allowancediscount to allowance_discount.
    context_object_name = 'allowance_discount'


class AllowanceDiscountListView(BaseListView):
    model = AllowanceDiscount
    template_name = 'atelier/allowance_discount_list.html'
    context_object_name = 'allowance_discount_list'


class AllowanceDiscountCreateView(SuperuserPermissionPreMixin, BaseCreateView):
    model = AllowanceDiscount
    form_class = AllowanceDiscountForm
    template_name = 'atelier/create_form.html'


class AllowanceDiscountUpdateView(SuperuserPermissionPreMixin, BaseUpdateView):
    model = AllowanceDiscount
    form_class = AllowanceDiscountForm
    template_name = 'atelier/create_form.html'


class AllowanceDiscountDeleteView(SuperuserPermissionPreMixin, BaseDeleteView):
    model = AllowanceDiscount
    success_url = reverse_lazy('atelier:allowance_discount_list')
    template_name = 'atelier/delete_form.html'
