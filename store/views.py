from django.db.models import Count, Sum
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
import json


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


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0}
        cartItems = order['get_cart_item']

    return render(request, 'store/cart.html', {'items': items, 'order': order, 'cartItems': cartItems})

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, Product= product)


    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)

    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == 'rall':
        orderItem.quantity = (orderItem.quantity - orderItem.quantity)




    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()






    return JsonResponse('item was added', safe= False)
