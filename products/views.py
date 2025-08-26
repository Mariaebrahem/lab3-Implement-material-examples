from django.shortcuts import render 
from.models import  products


def product(request):
    return render(request, 'products/product.html')

def products(request):
    return render(request, 'products/products.html',{'pro':   products.objects.all() })

