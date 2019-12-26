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

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.profile.is_tailor and not self.request.user.is_superuser:
            raise Http404()
        return super().dispatch(request, *args, **kwargs)


class BaseDetailView(LoginRequiredMixin, generic.DetailView):
    pass


class BaseListView(LoginRequiredMixin, generic.ListView):
    paginate_by = 10  # number of records on the one page


class BaseCreateView(SuperuserPermissionPreMixin, generic.CreateView):

    def form_valid(self, form):
        # assign base attributes to instances
        atelier = self.request.user.profile.atelier
        created_by = self.request.user
        last_updated_by = self.request.user
        atelier_object = form.save()
        atelier_object.atelier = atelier
        atelier_object.created_by = created_by
        atelier_object.last_updated_by = last_updated_by
        atelier_object.save()
        return super().form_valid(form)


class BaseUpdateView(SuperuserPermissionPreMixin, generic.UpdateView):
    def form_valid(self, form):
        # assign last_updated_by attribute to instance
        last_updated_by = self.request.user
        order = form.save()
        order.last_updated_by = last_updated_by
        order.save()
        return super().form_valid(form)


class BaseDeleteView(SuperuserPermissionPreMixin, generic.DeleteView):
    pass
