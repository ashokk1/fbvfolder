from django.contrib import admin
from .models import Product
class AdminProduct(admin.ModelAdmin):
    list_display = ['product_id','product_name','product_price','product_color']
admin.site.register(Product,AdminProduct)

