from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name=models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.category_name

# Create your models here.
class ProductsModel(models.Model):
    product_category= models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    product_desc=models.CharField(max_length=200)
    product_price=models.IntegerField(default=0)
    product_image=models.ImageField(default='Default.jpg',upload_to='uploads')
    trending=models.BooleanField(default=0)
    offer=models.BooleanField(default=0)


class CartModel(models.Model):
    products_name=models.CharField(max_length=10)
    products_price=models.IntegerField(default=0)
    products_desc=models.CharField(max_length=200)
    product_category=models.CharField(max_length=100)
    quantity=models.IntegerField(default=1)
    totalprice=models.IntegerField(default=0)
    host=models.ForeignKey(User,on_delete=models.CASCADE)