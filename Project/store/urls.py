from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Store Home"),
    path('listview/', views.store, name="listview"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
<<<<<<< HEAD
    path('detailview/', views.detailview, name="detailview"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
=======
    path('<int:product_id', views.detailview, name="detailview"),
>>>>>>> origin/views
]
