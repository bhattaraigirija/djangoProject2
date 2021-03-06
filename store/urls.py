from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('update_item/', views.updateItem, name='update_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('processOrder/', views.processOrder, name='processOrder'),
    path('login/', views.loginpage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutuser, name='logout'),
    path('search/', views.search, name='search'),
    path('administration/', views.adminmain, name='administration'),
    path('productm/', views.productm, name='productm'),
    path('productform/', views.addproduct, name='productform'),
    path('productform/', views.addproduct, name='productform'),
    path('updateproduct/<str:pk>/', views.updateproduct, name='updateproduct'),
    path('deleteproduct/<str:pk>/', views.deleteproduct, name='deleteproduct'),
    path('hospitalm/', views.hospitalm, name='hospitalm'),
    path('hospitalform/', views.addhospital, name='hospitalform'),
    path('deletehospital/<str:pk>/', views.deletehospital, name='deletehospital'),
    path('updatehospital/<str:pk>/', views.updatehospital, name='updatehospital'),
    path('orderm/', views.orderm, name='orderm'),
    path('deleteorder/<str:a>/<str:b>/', views.deleteorder, name='deleteorder'),
    path('userm/', views.userm, name='userm'),
    path('deleteuser/<str:pk>/', views.deleteuser, name='deleteuser')

]
