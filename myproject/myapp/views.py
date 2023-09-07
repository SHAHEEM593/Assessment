from django.db.models import Count
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Products, CustomerPreference, Orders
from django.shortcuts import render, redirect


def home(request):
    return render(request,'home.html')


def products_table(request):
    products = Products.objects.all()
    return render(request, 'products_table.html', {'products': products})

def preferences_table(request):
    preferences = CustomerPreference.objects.all()
    return render(request, 'preferences_table.html', {'preferences': preferences})

def orders_table(request):
    orders = Orders.objects.all()
    return render(request, 'orders_table.html', {'orders': orders})

def questions(request):
    if request.method == 'POST':
        selected_question = request.POST.get('question')
        if selected_question == 'most_popular_product':
            return redirect('most_popular_product')
        elif selected_question == 'customers_ordered_all_products':
            return redirect('customers_ordered_all_products')
        elif selected_question == 'customers_bought_inexpensive_items':
            return redirect('customers_bought_inexpensive_items')

    return render(request, 'questions.html')

def most_popular_product(request):
    products = Products.objects.annotate(preference_count=Count('customerpreference'))

    most_popular_product = products.order_by('-preference_count').first()

    context = {
        'most_popular_product': most_popular_product.name,
        'preference_count': most_popular_product.preference_count
    }

    return render(request, 'most_popular_product.html', context)
    

def customers_ordered_all_products(request):
    total_products = Products.objects.count()

    customer_orders = Orders.objects.values('customer_id').annotate(
        ordered_product_count=Count('product', distinct=True)
    )

    customers_ordered_all = customer_orders.filter(
        ordered_product_count=total_products
    )

    customer_ids_ordered_all = [customer['customer_id'] for customer in customers_ordered_all]

    if not customer_ids_ordered_all:
        customer_ids_ordered_all = ["None"]

    context = {'customers_ordered_all_products': customer_ids_ordered_all}
    return render(request, 'customers_ordered_all_products.html', context)


def customers_bought_inexpensive_items(request):
    inexpensive_threshold = 50.00

    customers = Orders.objects.values('customer_id').annotate(
        total_order_cost=Count('product__price')
    ).filter(total_order_cost__lt=inexpensive_threshold)

    customer_ids_bought_inexpensive = [customer['customer_id'] for customer in customers]

    context = {'customers_bought_inexpensive_items': customer_ids_bought_inexpensive}
    return render(request, 'customers_bought_inexpensive_items.html', context)
