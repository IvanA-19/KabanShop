from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# Модель, отвечающая за распределение товаров по категориям
class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name='Категория', null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    preview = models.ImageField(upload_to='media/category_photo', verbose_name='Фото-превью', null=True, blank=True)
    category_slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/shop/{self.category_slug}'

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


# Модель, отвечающая за карточку товара
class Product(models.Model):
    # Название товара
    title = models.CharField(max_length=300, verbose_name='Название', null=True, blank=True)
    # Описание
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    # Доступность товара в магазине
    availability = models.BooleanField(verbose_name='Доступен в магазине', null=True, blank=True)
    # Цена
    price = models.FloatField(verbose_name='Цена', null=True, blank=True)
    # Количество доступных единиц товара
    count = models.IntegerField(verbose_name='Количество доступных товаров', null=True, blank=True)
    # Привязываем товары к определенной категории(например бытовая техника, продукты и т.п.)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    # Слаг. Об этом читать в методичке
    product_slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/shop/{self.category.category_slug}/{self.product_slug}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id', 'title']


# Модель склада
class WareHouse(models.Model):
    # Если товар продается в магазине - значит он может потенциально быть на складе
    # Поэтому делаем связку с таблицей товаров
    # При удалении товара из магазина, т.е если он больше не продается - удаляем всю информацию о нем со склада
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    # Наличие товара на складе. True, если количество >0
    availability = models.BooleanField(verbose_name='Есть на складе')
    # Количество товара на складе
    count = models.IntegerField('Количество')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Товар на склад'
        verbose_name_plural = 'Товары на складе'


# Модель фотографий товаров
'''
    Фотографии товаров вынесены в отдельную модель ввиду того, что в карточке 
    одного товара может быть несколько фотографий данного товара. 
    Это позволит нам добавлять неограниченное количество фото и просто связывать их с конкретным товаром 
    с использованием внешнего ключа. Таким образом при получении нужного товара 
    у нас будет возможность получить все связанные с ним фото. 
    При удалении товара - все фото, которые связаны с ним будут удалены
'''


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    photo = models.ImageField(upload_to='media/product_photo', verbose_name='Фото товара', null=True, blank=True)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товара'


# Модель корзины
class Cart(models.Model):
    product = models.CharField(max_length=200, verbose_name='Товар', null=True, blank=True)
    price = models.FloatField(verbose_name='Цена', null=True, blank=True)
    count = models.IntegerField(verbose_name='Количество', null=True, blank=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Покупатель', null=True, blank=True)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары в корзине'
