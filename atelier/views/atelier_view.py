from django.http import Http404
from django.utils.translation import gettext_lazy as _


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

    def get(self, request, *args, **kwargs):
        """
        Override get function to add profile tailors and not tailors (sewers) quantity
         for each atelier into the context dictionary
        """
        num_tailors = Profile.objects.filter(is_tailor=True)
        num_sewers = Profile.objects.filter(is_tailor=False).count()
        ateliers = Atelier.objects.all()

        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.") % {
                    'class_name': self.__class__.__name__,
                })

        context = self.get_context_data()
        # for atelier in ateliers:
        #     context[atelier] = Profile.objects.filter(is_tailor=False, atelier=atelier).count()
        # context.update({'num_tailors': num_tailors,
        #                 'num_sewers': num_sewers})
        print(context)

        return self.render_to_response(context)


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
