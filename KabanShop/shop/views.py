from django.shortcuts import render


# Create your views here.
def index_view(request):
    return render(request, 'shop/index.html')


def shop_view(request):
    return render(request, 'shop/shop.html')


def cart_view(request):
    return render(request, 'shop/cart.html')
