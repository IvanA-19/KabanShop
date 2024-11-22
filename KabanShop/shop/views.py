from django.shortcuts import render
from .models import *


# Create your views here.
def index_view(request):
    return render(request, 'shop/index.html')


def shop_view(request):
    categories = Category.objects.order_by('title')

    context = {'categories': categories}
    return render(request, 'shop/shop.html', context=context)


# Это закодим потом
def cart_view(request):
    return render(request, 'shop/cart.html')


def category_view(request, category_slug):
    category = Category.objects.get(category_slug=category_slug)
    products = Product.objects.filter(category_id=category.id).order_by('title')

    context = {'category': category, 'products': products}

    return render(request, 'shop/category.html', context=context)


def product_view(request, category_slug, product_slug):
    # Получаем данные из БД с использованием фильтраций в селектах.
    category = Category.objects.get(category_slug=category_slug)
    product = Product.objects.get(product_slug=product_slug)
    product_photo = ProductPhoto.objects.filter(product_id=product.id)

    # Формируем словарь, содержащий данные, которые будут переданы в ответе с сервера
    # при формировании страницы
    context = {'category': category, 'product': product, 'product_photo': product_photo}

    # Возвращаем ответ от сервера в виде шаблона, который отображает страницу и данных из БД
    return render(request, 'shop/product.html', context=context)

