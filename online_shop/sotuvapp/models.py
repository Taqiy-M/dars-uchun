from django.db import models

# Create your models here.
from userapp.models import Account
from asosiy.models import Product


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    discount = models.PositiveIntegerField(default=0)
    cost = models.PositiveIntegerField(default=0)

    def __str__(self):
        if self.product:
            return self.product.name
        else:
            return self


class Cart(models.Model):
    order = models.ManyToManyField(Order, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    cost = models.PositiveBigIntegerField(default=0)
    ordered_time = models.DateTimeField(null=True, default=None, blank=True)
    delivered_time = models.DateTimeField(null=True, default=None, blank=True)
    history = models.BooleanField(default=False)

    def __str__(self):
        return self.account.ism














