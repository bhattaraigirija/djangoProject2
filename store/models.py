from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, )
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(blank=True, upload_to='images/')
    description = models.CharField(max_length=2000, null=True)
    stock = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
            return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_of_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __dir__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_item(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.Product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Hospital(models.Model):
    name = models.CharField(max_length=200, null=True)
    info = models.CharField(max_length=2000, null=True)
    address = models.CharField(max_length=200, null=True)
    disease = models.CharField(max_length=2000, null=True)
    state = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
            return url
