from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'atelier'
'''
path() argument: name¶
Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates. 
This powerful feature allows you to make global changes to the URL patterns of your project 
while only touching a single file.
'''
urlpatterns = [
    path('', views.index, name='index'),
    path('client/', views.ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('client/add/', views.ClientCreateView.as_view(), name='client_form'),
    path('client/<int:pk>/edit/', views.ClientUpdateView.as_view(), name='client_update_form'),
    path('client/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client_delete_form'),
    path('product/', views.ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', views.ProductCreateView.as_view(), name='product_form'),
    path('product/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_update_form'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete_form'),
    path('order/', views.OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('order/add/', views.OrderCreateView.as_view(), name='order_form'),
    path('order/<int:pk>/edit/', views.OrderUpdateView.as_view(), name='order_update_form'),
    path('order/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order_delete_form'),
    path('allowance_discount/', views.AllowanceDiscountListView.as_view(), name='allowance_discount_list'),
    path('allowance_discount/<int:pk>/', views.AllowanceDiscountDetailView.as_view(), name='allowance_discount_detail'),
    path('allowance_discount/add/', views.AllowanceDiscountCreateView.as_view(), name='allowance_discount_form'),
    path('allowance_discount/<int:pk>/edit/', views.AllowanceDiscountUpdateView.as_view(),
         name='allowance_discount_update_form'),
    path('allowance_discount/<int:pk>/delete/', views.AllowanceDiscountDeleteView.as_view(),
         name='allowance_discount_delete_form'),
    path('complication_element/', views.ComplicationElementListView.as_view(), name='complication_element_list'),
    path('complication_element/<int:pk>/', views.ComplicationElementDetailView.as_view(),
         name='complication_element_detail'),
    path('complication_element/add/', views.ComplicationElementCreateView.as_view(), name='complication_element_form'),
    path('complication_element/<int:pk>/edit/', views.ComplicationElementUpdateView.as_view(),
         name='complication_element_update_form'),
    path('complication_element/<int:pk>/delete/', views.ComplicationElementDeleteView.as_view(),
         name='complication_element_delete_form'),
    path('fabric/', views.FabricListView.as_view(), name='fabric_list'),
    path('fabric/<int:pk>/', views.FabricDetailView.as_view(), name='fabric_detail'),
    path('fabric/add/', views.FabricCreateView.as_view(), name='fabric_form'),
    path('fabric/<int:pk>/edit/', views.FabricUpdateView.as_view(), name='fabric_update_form'),
    path('fabric/<int:pk>/delete/', views.FabricDeleteView.as_view(), name='fabric_delete_form'),
    path('minimal_style/', views.MinimalStyleListView.as_view(), name='minimal_style_list'),
    path('minimal_style/<int:pk>/', views.MinimalStyleDetailView.as_view(), name='minimal_style_detail'),
    path('minimal_style/add/', views.MinimalStyleCreateView.as_view(), name='minimal_style_form'),
    path('minimal_style/<int:pk>/edit/', views.MinimalStyleUpdateView.as_view(), name='minimal_style_update_form'),
    path('minimal_style/<int:pk>/delete/', views.MinimalStyleDeleteView.as_view(), name='minimal_style_delete_form'),
    path('atelier/', views.AtelierListView.as_view(), name='atelier_list'),
    path('atelier/<int:pk>/', views.AtelierDetailView.as_view(), name='atelier_detail'),
    path('atelier/add/', views.AtelierCreateView.as_view(), name='atelier_form'),
    path('atelier/<int:pk>/edit/', views.AtelierUpdateView.as_view(), name='atelier_update_form'),
    path('atelier/<int:pk>/delete/', views.AtelierDeleteView.as_view(), name='atelier_delete_form'),
    path('profile/', views.ProfileListView.as_view(), name='profile_list'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/add/', views.ProfileCreateView.as_view(), name='profile_form'),
    path('profile/<int:pk>/edit/', views.ProfileChangeView.as_view(), name='profile_update_form'),
    path('profile/<int:pk>/delete/', views.ProfileDeleteView.as_view(), name='profile_delete_form'),
    # path('profile/<int:pk>/edit/', views.change_profile, name='profile_update_form'),
]
