from django.urls import path
from . import views

app_name = 'atelier'
urlpatterns = [
    path('product/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add/', views.ClientCreateView.as_view(), name='client_form'),
    path('<int:pk>/edit/', views.ClientUpdateView.as_view(), name='client_update_form'),
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:product_id>/vote/', views.vote, name='vote'),
]
