from django.shortcuts import render

from django.http import HttpResponse 

def home(response):
    return render(response,'home.html')


def product(response):
    return render(response,'product.html')


def cart(response):
    return render(response,'cart.html')


