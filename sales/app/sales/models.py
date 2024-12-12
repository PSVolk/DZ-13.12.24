from datetime import datetime

from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    lastname = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField()

class Seller(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    date = models.DateField()
    seller_position = ('seller', 'S'), ('superseller', 'SS'), ('manager', 'M')
    position = models.TextField(choices=seller_position)

class Item(models.Model):
    name = models.CharField(max_length=30)
    info = models.TextField()


class Order(models.Model):
    date = models.DateTimeField(default=datetime.now())
    total = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    item = models.ManyToManyField(Item)

# class Order_positions(models.Model):
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)