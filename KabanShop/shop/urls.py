from django.urls import path
from .import views


app_name = 'shop'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('shop/', views.shop_view, name='products'),
    path('cart/', views.cart_view, name='cart'),
    path('shop/<slug:category_slug>/', views.category_view, name='category'),
    path('shop/<slug:category_slug>/<slug:product_slug>/', views.product_view, name='product'),
    path('shop/<slug:category_slug>/<slug:product_slug>/to_cart', views.order_view, name='order'),
    path('shop/<slug:category_slug>/<slug:product_slug>/to_cart/order_error', views.order_error_view,
         name='order_error'),
    path('shop/<slug:category_slug>/<slug:product_slug>/to_cart/ordered', views.added_to_cart_view,
         name='added_to_cart'),
    path('cart/delete_product/<int:product_id>', views.delete_product_view, name='delete_product'),
    path('cart/ordered/>', views.ordered_view, name='ordered')
]

