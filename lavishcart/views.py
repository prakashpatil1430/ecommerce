from django.shortcuts import render
from store.models import Product
from category.models import Category


def home(request):
    products = Product.objects.filter(is_available=True)
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)
