from django.contrib import admin
from .models import Store, Product

# Register your models here.


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'created_date')
    list_display_links = ('name', 'address', 'email')
    search_fields = ('name', 'address')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'manufacturer', 'price', 'store')
    list_display_links = ('name', 'description', 'manufacturer', 'price')
    search_fields = ('name', 'description', 'manufacturer')


admin.site.register(Store, StoreAdmin)
admin.site.register(Product, ProductAdmin)