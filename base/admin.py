from django.contrib import admin

# Register your models here.
from .models import ProductsModel,Category

class categoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name']

admin.site.register(Category,categoryAdmin) 

class ProductsAdmin(admin.ModelAdmin):
    list_display=['id','product_name','product_desc','product_price']

admin.site.register(ProductsModel,ProductsAdmin)