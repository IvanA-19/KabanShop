from django import forms
from django.contrib.auth.models import User
from .models import Cart


class OrderForm(forms.ModelForm):
    count = forms.IntegerField(min_value=0, label='Количество')

    class Meta:
        model = Cart
        fields = ['count']

