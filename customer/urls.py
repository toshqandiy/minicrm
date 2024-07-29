from django.urls import path

from . import views

urlpatterns = [
    path('', views.customers_list, name='customers_list'),
    path('<int:pk>', views.customers_detail, name='customers_detail'),
    path('add/', views.customers_add, name='customers_add'),
    path('<int:pk>/edit/', views.customers_edit, name='customers_edit'),
    path('<int:pk>/delete/', views.customers_delete, name='customers_delete'),
]