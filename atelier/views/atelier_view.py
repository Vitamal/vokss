from atelier.models import Atelier, Profile
from django.views import generic
from atelier.forms import AtelierForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin


class AtelierDetailView(UserPassesTestMixin, generic.DetailView):
    model = Atelier
    fields = '__all__'

    def test_func(self):
        """
        check permissions in class-based views with the help of UserPassesTestMixin and test_funk
        """
        return self.request.user.is_superuser


class AtelierListView(UserPassesTestMixin, generic.ListView):
    model = Atelier
    paginate_by = 10  # number of records on the one page

    def test_func(self):
        """
        check permissions in class-based views with the help of UserPassesTestMixin and test_funk
        """
        return self.request.user.is_superuser


class AtelierCreateView(UserPassesTestMixin, generic.CreateView):
    model = Atelier
    form_class = AtelierForm
    template_name = 'atelier/create_form.html'

    def test_func(self):
        """
        check permissions in class-based views with the help of UserPassesTestMixin and test_funk
        """
        return self.request.user.is_superuser


class AtelierUpdateView(UserPassesTestMixin, generic.UpdateView):
    model = Atelier
    form_class = AtelierForm
    template_name = 'atelier/create_form.html'

    def test_func(self):
        """
        check permissions in class-based views with the help of UserPassesTestMixin and test_funk
        """
        return self.request.user.is_superuser


class AtelierDeleteView(UserPassesTestMixin, generic.DeleteView):
    model = Atelier
    success_url = reverse_lazy('atelier:atelier_list')
    template_name = 'atelier/delete_form.html'

    def test_func(self):
        """
        check permissions in class-based views with the help of UserPassesTestMixin and test_funk
        """
        return self.request.user.is_superuser
