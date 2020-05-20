from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Store Home"),
    path('listview', views.store, name="listview"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('<int:product_id>', views.detailview, name="detailview"),
<<<<<<< HEAD
    path('<str:category_name>', views.category, name="category"),
=======
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
>>>>>>> 79b2fe8d49dae5b0733d687117cfea38936823fa
]
