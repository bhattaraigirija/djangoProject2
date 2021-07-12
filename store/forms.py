from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Product
from .models import Hospital


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class productform(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class hospitalform(ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'
