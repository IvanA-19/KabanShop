from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from users.models import UserProfile


# Create your views here.
def index_view(request):
    return render(request, 'shop/index.html')


def shop_view(request):
    categories = Category.objects.order_by('title')

    context = {'categories': categories}
    return render(request, 'shop/shop.html', context=context)


@login_required(login_url='users:login')
def cart_view(request):
    products_in_cart = Cart.objects.filter(buyer_id=request.user)
    final_price = 0
    for product in products_in_cart:
        final_price += product.price * product.count
    context = {'products': products_in_cart, 'final_price':final_price}
    return render(request, 'shop/cart.html', context=context)


def category_view(request, category_slug):
    category = Category.objects.get(category_slug=category_slug)
    products = Product.objects.filter(category_id=category.id).order_by('title')

    context = {'category': category, 'products': products}

    return render(request, 'shop/category.html', context=context)


def product_view(request, category_slug, product_slug):
    # Получаем данные из БД с использованием фильтраций в селектах.
    category = Category.objects.get(category_slug=category_slug)
    product = Product.objects.get(product_slug=product_slug)
    product_photo = ProductPhoto.objects.prefetch_related('product').filter(product_id=product.id)

    # Формируем словарь, содержащий данные, которые будут переданы в ответе с сервера
    # при формировании страницы
    context = {'category': category, 'product': product, 'product_photo': product_photo}

    # Возвращаем ответ от сервера в виде шаблона, который отображает страницу и данных из БД
    return render(request, 'shop/product.html', context=context)


@login_required(login_url='users:login')
def order_error_view(request, category_slug, product_slug):
    category = Category.objects.get(category_slug=category_slug)
    product = Product.objects.get(product_slug=product_slug)

    context = {'category': category, 'product': product}

    return render(request, 'shop/order_error.html', context=context)


@login_required(login_url='users:login')
def added_to_cart_view(request, category_slug, product_slug):
    category = Category.objects.get(category_slug=category_slug)
    product = Product.objects.get(product_slug=product_slug)
    context = {'category': category, 'product': product}
    return render(request, 'shop/added_to_cart.html', context=context)


@login_required(login_url='users:login')
def order_view(request, category_slug, product_slug):
    product = Product.objects.get(product_slug=product_slug)

    error = False
    try:
        product_in_ware_house = WareHouse.objects.get(product_id=product.id)
    except WareHouse.DoesNotExist:
        error = True
    finally:
        if error:
            product_in_ware_house = None
        else:
            product_in_ware_house = WareHouse.objects.get(product_id = product.id)

    category = Category.objects.get(category_slug=category_slug)
    available_product_count = product.count
    if product_in_ware_house:
        available_product_count += product_in_ware_house.count

    if request.method != 'POST':
        form = OrderForm()
    else:
        form = OrderForm(data=request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.product = product.title
            new_order.price = product.price
            new_order.buyer = request.user
            if new_order.count > available_product_count:
                return redirect('shop:order_error', category.category_slug, product.product_slug)
            elif new_order.count < available_product_count:
                if new_order.count < product.count:
                    product.count -= new_order.count
                    product.save()
                elif product.count - new_order.count < 10:
                    product_in_ware_house = WareHouse.objects.get(product_id=product.id)
                    product.count = available_product_count - new_order.count
                    product_in_ware_house.count = 0
                    product_in_ware_house.availability = False
                    product.save()
                    product_in_ware_house.save()
            else:
                product_in_ware_house = WareHouse.objects.get(product_id=product.id)
                new_order.count = available_product_count
                product.delete()
                if product_in_ware_house:
                    product_in_ware_house.count = 0
                    product_in_ware_house.availability = False
                    product_in_ware_house.save()
            form.save()
            return redirect('shop:added_to_cart', category.category_slug, product.product_slug)
    context = {'category': category, 'product': product, 'form': form}
    return render(request, 'shop/order.html', context=context)


@login_required(login_url='users:login')
def delete_product_view(request, product_id):
    product = Cart.objects.get(id=product_id)
    product_in_shop = Product.objects.get(title=product.product)
    product_in_shop.count += product.count
    product_in_shop.save()
    product.delete()
    return redirect('shop:cart')


@login_required(login_url='users:login')
def fill_profile_view(request):
    return render(request, 'shop/fill_profile.html')


@login_required(login_url='users:login')
def ordered_view(request):
    user_profile = UserProfile.objects.get(email=request.user.email)
    if user_profile:
        if user_profile.email and user_profile.phone_number and user_profile.address:
            products = Cart.objects.filter(buyer_id=request.user)
            for product in products:
                product.delete()
            return render(request, 'shop/ordered.html')

    return redirect('shop:fill_profile')
