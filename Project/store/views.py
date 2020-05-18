from django.shortcuts import get_object_or_404, render
from .models import *
from django.http import Http404

# Create your views here.
def home(request):
    context = {}
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
        order, created = Order.object.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else: 
        items = []  
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {
        'items': items,
        'order': order,
    }
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

