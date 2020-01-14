from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views import generic


class SuperuserPermissionPreMixin(object):
    """
    check permissions for superuser
    """

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise Http404()
        return super().dispatch(request, *args, **kwargs)


class AtelierFilterObjectsPreMixin:
    """
    to show objects in established atelier only (for superuser all objects are showed)
    """

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.model.objects.all()  # admin user access all objects
        else:
            # ordinary user has access to objects of his atelier only
            return self.model.objects.filter(atelier=self.request.user.profile.atelier)


class TailorPermissionPreMixin:
    """
    check permissions for tailor or superuser
    """

    # def dispatch(self, request, *args, **kwargs):
    #     if self.request.user.is_anonymous or not self.request.user.profile.is_tailor and not self.request.user.is_superuser:
    #         raise Http404()
    #     return super().dispatch(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            raise Http404()
        elif self.request.user.is_superuser or self.request.user.profile.is_tailor:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404()


class BaseDetailView(LoginRequiredMixin, generic.DetailView):
    pass


class BaseListView(LoginRequiredMixin, generic.ListView):
    paginate_by = 10  # number of records on the one page


class BaseCreateView(LoginRequiredMixin, generic.CreateView):
    def form_valid(self, form):
        # assign atelier, created_by and last_updated_by attributes to instances
        atelier_object = form.save(commit=False)  ## Create, but don't save the new instance.
        atelier = self.request.user.profile.atelier
        created_by = self.request.user
        atelier_object.created_by = created_by
        atelier_object.last_updated_by = created_by
        atelier_object.atelier = atelier
        atelier_object.save()
        return super().form_valid(form)


class BaseUpdateView(LoginRequiredMixin, generic.UpdateView):
    def form_valid(self, form):
        # assign last_updated_by attribute to instance
        last_updated_by = self.request.user
        atelier_object = form.save()
        atelier_object.last_updated_by = last_updated_by
        atelier_object.save()
        return super().form_valid(form)


class BaseDeleteView(LoginRequiredMixin, generic.DeleteView):
    pass
