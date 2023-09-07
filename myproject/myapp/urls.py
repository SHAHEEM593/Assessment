from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('questions/', views.questions, name='questions'),
    path('products/', views.products_table, name='products_table'),
    path('preferences/', views.preferences_table, name='preferences_table'),
    path('orders/', views.orders_table, name='orders_table'),
    path('most-popular-product/', views.most_popular_product, name='most_popular_product'),
    path('customers-ordered-all-products/', views.customers_ordered_all_products, name='customers_ordered_all_products'),
    path('customers-bought-inexpensive-items/', views.customers_bought_inexpensive_items, name='customers_bought_inexpensive_items'),
]
