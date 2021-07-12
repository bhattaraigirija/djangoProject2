from django.db.models import Count, Sum
from django.shortcuts import render, redirect
from .models import *


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:

        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0}
        cartItems = order['get_cart_item']
    products = Product.objects.all()

    return render(request, 'store/store.html', {'products': products, 'cartItems': cartItems, 'items': items})
