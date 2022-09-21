from django.db import models
from userapp.models import Account

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    photo = models.FileField(upload_to="category")

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    photo = models.FileField(upload_to="sub_category")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    producer = models.CharField(max_length=50)
    guarantee = models.CharField(max_length=50)
    delivery = models.CharField(max_length=50)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    photo = models.FileField(upload_to="products", blank=True, null=True, default=None)
    unit = models.CharField(null=True, blank=True, default=None, max_length=15)


    def __str__(self):
        return self.name



class Comment(models.Model):
    comment = models.TextField()
    rate = models.IntegerField(default=3)
    sana = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

