from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from users.models import UserProfile

from string import Template
from django.utils.safestring import mark_safe
from django.forms import ImageField


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, label='Имя пользователя')
    first_name = forms.CharField(max_length=100, label='Имя')
    last_name = forms.CharField(max_length=100, label='Фамилия')
    email = forms.EmailField(max_length=100, label='Электронная почта')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Этот адрес электронной почты уже занят!")
        return email

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class EditProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=250, label='Имя пользователя')
    first_name = forms.CharField(max_length=100, label='Имя')
    last_name = forms.CharField(max_length=100, label='Фамилия')
    email = forms.EmailField(max_length=100, label='Электронная почта')
    phone_number = forms.CharField(max_length=30, label='Номер телефона', required=False)
    avatar = forms.ImageField(label='Аватар')

    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'avatar']






