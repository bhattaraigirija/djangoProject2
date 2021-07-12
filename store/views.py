from django.db.models import Count, Sum
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
import json
import datetime
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, Product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)

    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == 'rall':
        orderItem.quantity = (orderItem.quantity - orderItem.quantity)

    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('item was added', safe=False)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0}
        cartItems = order['get_cart_item']
    return render(request, 'store/checkout.html', {'items': items, 'order': order, 'cartItems': cartItems})


def processOrder(request):
    transactionId = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    total = (data['form']['total'])
    Order.transaction_id = transactionId
    if total == Order.get_cart_total:
        Order.complete = True
        Order.save()

    if request.user.is_authenticated:
        customer = request.user.customer
    else:
        print('User not authenticated')

    print("Data:", request.body)

    return JsonResponse('payment complete', safe=False)


def register(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                # mail= form.cleaned_data.get('email')
                # cutomer_obj=Customer.objects.create(user=request.user, name=user, email=mail)
                # cutomer_obj.save()

                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        return render(request, 'store/register.html', {'form': form})


def loginpage(request):
    if request.user.is_authenticated:

        return redirect('store')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                login(request, user)
                mail = request.user.email
                if Customer.objects.filter(user=request.user).exists() == False:
                    cutomer_obj = Customer.objects.create(user=request.user, name=username, email=mail)
                    cutomer_obj.save()

                return redirect('store')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'store/login.html', context)


def logoutuser(request):
    logout(request)
    return redirect('login')
