from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customers, Order, Roles


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BarbershopOrders(ModelForm):
    class Meta:
        model = Order
        fields = ['barber', 'day', 'time', 'haircut_name']


class CustomerInformation(ModelForm):
    class Meta:
        model = Customers
        fields = ['name', 'surname', 'info']


class TimeForm(forms.Form):
    category_time = forms.ChoiceField(choices=Order.TIME)