from django import forms
from datetime import datetime

from .models import Customer, Seller


class UserForm(forms.Form):
    name = forms.CharField(max_length=30)
    age = forms.IntegerField()

class SellerForm(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=30)
    email = forms.EmailField()
    seller_position = ('seller', 'S'), ('superseller', 'SS'), ('manager', 'M')
    position = forms.ChoiceField(choices=seller_position)

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=30)
    age = forms.IntegerField()
    lastname = forms.CharField(max_length=30)
    phone = forms.IntegerField()
    email = forms.EmailField()

class ItemForm(forms.Form):
    name = forms.CharField(max_length=30)
    price = forms.IntegerField()


class OrderForm(forms.Form):
    date = forms.DateTimeField()
    total = forms.IntegerField()
    # customer = forms.ChoiceField(choices=tuple(((c.id, c.name) for c in Customer.objects.all())))
    # seller =  forms.ChoiceField(choices=tuple(((c.id, c.name) for c in Seller.objects.all())))
    # item = forms.ManyToManyField(Item)