from django.urls import path
from . import views
from .views import Customer, CustomerListView

urlpatterns = [
    path('Customer', Customer),
    path('login1', views.login1, name='login1'),
    path('index', views.index, name='index'),
    path('gpon', views.gpon, name='gpon'),
    path('welcome', views.welcome, name='welcome'),
    path('organic', views.organic, name='organic'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('details/<id>', views.details, name='details'),
    path('customers_on_splitter', views.customers_on_splitter, name='customers_on_splitter'),
    path('register', views.register, name='register'),
    path('show_customers', views.show_customers, name='show_customers'),
    path('snippet_list', views.CustomerListView, name='snippet_list'),
    path('add_customer', views.add_customer, name="add_customer"),
    path('add_splitter', views.add_splitter, name="add_splitter"),
    path('customer_details/<id>', views.customer_details, name="customer_details"),
]
