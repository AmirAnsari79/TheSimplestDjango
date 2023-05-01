from django.contrib import admin
from django.contrib.admin import register

from catalogue.models import *


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'product_type', 'is_active', 'upc', 'title', 'category', 'brand']
    list_filter = ['is_active']
    search_fields = ['upc', 'title', 'category__name', 'brand__name']
    list_display_links = ['title', 'product_type']
    list_editable = ['is_active']


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductType)
# admin.site.register(Product, ProductAdmin)
