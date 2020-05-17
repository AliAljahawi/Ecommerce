from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name="Store Home"),
    path('listview', views.store, name="listview"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('detailview', views.detailview, name="detailview"),
]
