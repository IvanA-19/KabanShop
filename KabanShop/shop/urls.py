from django.urls import path
from .import views


app_name = 'shop'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('shop/', views.shop_view, name='products'),
    path('cart/', views.cart_view, name='cart'),

]

