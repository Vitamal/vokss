from django.urls import path
from . import views

app_name = 'atelier'
urlpatterns = [
    path('', views.index, name='index'),
    path('client/', views.ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('client/add/', views.ClientCreateView.as_view(), name='client_form'),
    path('client/<int:pk>/edit/', views.ClientUpdateView.as_view(), name='client_update_form'),
    # path('', views.IndexView.as_view(), name='index'),
    path('product/', views.ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('order/', views.OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
]
