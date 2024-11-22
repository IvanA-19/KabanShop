from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=300, verbose_name='Имя пользователя')
    first_name = models.CharField(max_length=300, verbose_name='Имя')
    last_name = models.CharField(max_length=300, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=30, verbose_name='Номер телефона', blank=True, null=True)
    avatar = models.ImageField(upload_to='media/user_avatars', verbose_name='Аватар', blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

