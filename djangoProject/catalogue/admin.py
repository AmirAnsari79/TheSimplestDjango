from django.contrib import admin
from django.contrib.admin import register

from catalogue.models import *


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'product_type', 'is_active', 'upc', 'title', 'category', 'brand']
    list_filter = ['is_active']
    search_fields = ['upc', 'title', 'category__name', 'brand__name']
    list_display_links = ['title', 'product_type']
    list_editable = ['is_active']
    actions = ('activate_all',)

    def activate_all(self, request, queryset):
        pass


@register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_display = ('product', 'value', 'attribute')
    list_editable = ('value',)
    list_display_links = ('product', 'attribute',)


@register(ProductAttribute)
class ProductAttribute(admin.ModelAdmin):
    list_display = ('title', 'product_type',)
    list_filter = ('product_type',)


@register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc',)
    inlines = [ProductAttributeInline]


admin.site.register(Brand)
admin.site.register(Category)

# admin.site.register(Product, ProductAdmin)
