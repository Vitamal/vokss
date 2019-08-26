from django.shortcuts import get_object_or_404, render
from atelier.models import Client, Product, Fabric, Order


def index(request):
    '''
    Home page view function
    '''
    num_fabrics = Fabric.objects.all().count()
    num_products = Product.objects.all().count()
    num_clients = Client.objects.all().count()
    num_orders = Order.objects.all().count()

    return render(request, 'atelier/index.html', context={'num_fabrics': num_fabrics, 'num_products': num_products,
                                                          'num_clients': num_clients, 'num_orders': num_orders})
