from django.shortcuts import get_object_or_404, render
from atelier.models import Profile, Client, Product, Fabric, Order, ComplicationElement, MinimalStyle, \
    AllowanceDiscount, Atelier
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
def index(request):
    """
    Home page view
    """

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    if request.user.is_superuser:
        '''
        Home page view for superuser
        '''
        num_ateliers = Atelier.objects.all().count()
        num_profiles = Profile.objects.all().count()
        num_fabrics = Fabric.objects.all().count()
        num_products = Product.objects.all().count()
        num_clients = Client.objects.all().count()
        num_orders = Order.objects.all().count()
        num_complication_element = ComplicationElement.objects.all().count()
        num_minimal_style = MinimalStyle.objects.all().count()
        num_allowance_discount = AllowanceDiscount.objects.all().count()


        return render(request, 'atelier/index.html', context={
            'num_ateliers': num_ateliers,
            'num_profiles': num_profiles,
            'num_fabrics': num_fabrics,
            'num_products': num_products,
            'num_clients': num_clients,
            'num_orders': num_orders,
            'num_allowance_discount': num_allowance_discount,
            'num_complication_element': num_complication_element,
            'num_minimal_style': num_minimal_style,
            'num_visits': num_visits,
        })
    else:
        '''
        Home page view for all users
        '''
        atelier = request.user.profile.atelier
        num_products = Product.objects.filter(atelier=atelier).count()
        num_clients = Client.objects.filter(atelier=atelier).count()
        num_orders = Order.objects.filter(atelier=atelier).count()

        return render(request, 'atelier/index.html', context={
            'atelier': atelier,
            'num_products': num_products,
            'num_clients': num_clients,
            'num_orders': num_orders,
            'num_visits': num_visits,
        })
