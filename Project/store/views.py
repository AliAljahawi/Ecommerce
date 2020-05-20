<<<<<<< HEAD
from django.shortcuts import get_object_or_404, render, redirect
=======
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login
>>>>>>> master
from .models import *
from django.http import Http404
from django.contrib.auth import authenticate , login

# Create your views here.
def home(request):
    products = Product.objects.all()[:3]
    context = {'products':products}
    return render(request, 'store/home.html', context)

def store(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/listview.html', context)

def detailview(request, product_id):
    # try:
    #     product = Product.object.get(pk=product_id)
    # except Product.DoesNotExist:
    #     raise Http404("Product does not exist")    
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
  
    return render(request, 'store/detailview.html', context)    

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
<<<<<<< HEAD
        order, created = Order.object.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else: 
        return redirect('login')
    context = {
        'items': items,
        'order': order,
    }
=======
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        return redirect('login')
        
    context = {'items':items , 'order':order}
>>>>>>> master
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.object.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else: 
        items = []  
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'store/checkout.html', context)

<<<<<<< HEAD
def category(request, category_name):
    products = Product.objects.filter(category=category_name)
    context = {
        'products': products,
    }
    return render(request, 'store/category.html', context)

    
=======
def detailview(request):
    context = {}
    return render(request, 'store/detailview.html', context)

>>>>>>> master
def signup(request):
    if request.method == 'GET':
        return render(request, 'store/signup.html')

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        name = request.POST["name"]
        email = request.POST["email"]
        address = request.POST["address"]
        city = request.POST["city"]
        phone_number = request.POST["phone_number"]

        user = User.objects.create_user(username , email , password)
        customer = Customer(user=user,name=name,email=email,address=address,city=city,phone_number=phone_number)
        customer.save()
        return redirect('Store Home')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'store/login.html')

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
<<<<<<< HEAD
        user = authenticate(request,username=username, password=password)
=======
        user = authenticate(request,username=username, password=username)
>>>>>>> master
        if user is not None:
            login(request, user)
            return redirect('Store Home')
        else:
            return render(request, 'store/login.html')

def logout_view(request):
    logout(request)
<<<<<<< HEAD
    return redirect('Store Home')
=======
    return redirect('Store Home')
>>>>>>> master
