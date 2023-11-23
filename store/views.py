from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category


def store(request, category_slug=None):
    products = None
    category = None
    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=category, is_available=True)
    else:
        products = Product.objects.filter(is_available=True)

    products_count = products.count()
    context = {
        'products': products,
        'products_count': products_count,
    }
    return render(request, 'store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product
    }
    return render(request, 'store/product_detail.html', context)
