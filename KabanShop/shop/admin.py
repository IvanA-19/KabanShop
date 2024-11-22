from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'availability', 'count', 'price']
    list_display_links = ['title', 'category']
    search_fields = ['title', 'category']
    prepopulated_fields = {'product_slug': ('title', )}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_html_preview']
    list_display_links = ['title']
    search_fields = ['title']
    prepopulated_fields = {'category_slug': ('title',)}
    readonly_fields = ('get_html_preview', )

    def get_html_preview(self, obj):
        if obj.preview:
            return mark_safe(f'<img src="{obj.preview.url}" width=50px>')

    get_html_preview.short_description = 'Превью'


class WareHouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'availability', 'count']
    list_display_links = ['product']
    search_fields = ['product']


class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'get_html_photo']
    list_display_links = ['product']
    search_fields = ['product']
    readonly_fields = ('get_html_photo', )

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=50px>')

    get_html_photo.short_description = 'Фото'


class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'count', 'price', 'buyer']
    list_display_links = ['product', 'buyer']
    search_fields = ['product', 'buyer']


admin.site.register(Product, ProductAdmin)
admin.site.register(WareHouse, WareHouseAdmin)
admin.site.register(ProductPhoto, ProductPhotoAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Category, CategoryAdmin)
