from django.shortcuts import get_object_or_404, render
from atelier.models import Client, Product, Fabric, Order, ComplicationElement, MinimalStyle, AllowanceDiscount


def index(request):
    '''
    Home page view function
    '''
    from django.utils import translation

    num_fabrics = Fabric.objects.all().count()
    num_products = Product.objects.all().count()
    num_clients = Client.objects.all().count()
    num_orders = Order.objects.all().count()
    num_complication_element = ComplicationElement.objects.all().count()
    num_minimal_style = MinimalStyle.objects.all().count()
    num_allowance_discount = AllowanceDiscount.objects.all().count()

    return render(request, 'atelier/index.html', context={'num_fabrics': num_fabrics, 'num_products': num_products,
                                                          'num_clients': num_clients, 'num_orders': num_orders,
                                                          'num_allowance_discount': num_allowance_discount,
                                                          'num_complication_element': num_complication_element,
                                                          'num_minimal_style': num_minimal_style})
