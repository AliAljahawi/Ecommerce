from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    context = {}
    return render(request, 'store/home.html', context)

def store(request):
    context = {}
    return render(request, 'store/listview.html', context)

def cart(request):
    #for me absy
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def detailview(request):
    context = {}
    return render(request, 'store/detailview.html', context)