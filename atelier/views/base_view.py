from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class BaseDetailView(LoginRequiredMixin, generic.DetailView):
    pass

class BaseListView(LoginRequiredMixin, generic.ListView):
    paginate_by = 10  # number of records on the one page

