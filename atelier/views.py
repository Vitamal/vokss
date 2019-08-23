from django.shortcuts import get_object_or_404, render
from .models import MyClient, Product
from django.views.generic import CreateView
from django.views.generic import UpdateView
from atelier.forms import ClientForm
from django.views.generic import ListView

class ClientListView(ListView):
    model = MyClient


class ClientCreateView(CreateView):
    model = MyClient
    fields = ('first_name', 'last_name', 'tel_number', 'place')
    template_name = 'atelier/client_form.html'

class ClientUpdateView(UpdateView):
    model = MyClient
    form_class = ClientForm
    template_name = 'atelier/client_update_form.html'

def product_list(request):
    products = Product.objects.all()
    return render(request, 'atelier/product_list.html', {'products': products})

def product_detail(request, pk):
    details = get_object_or_404(Product, pk=pk)
    return render(request, 'atelier/product_detail.html', {'details': details})

'''
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'atelier/product_list.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.order_by('name')


class DetailView(generic.DetailView):
    model = Product
    template_name = 'atelier/detail.html'

class ResultsView(generic.DetailView):
    model = Product
    template_name = 'atelier/results.html'

def vote(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    try:
        selected_myorder = product.myorder_set.get(pk=request.POST['product'])
    except (KeyError, MyOrder.DoesNotExist):
    # Redisplay the question voting form.
        return render(request, 'atelier/detail.html', {'product': product,'error_message': "You didn't select an order.",  })
    else:
        selected_myorder.votes += 1
        selected_myorder.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('atelier:results', args=(product.id,)))
'''