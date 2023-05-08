from django.db import models


class ProductType(models.Model):
    title = models.CharField(max_length=32, blank=True, null=True)
    desc = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class ProductAttribute(models.Model):
    INTEGER = 1
    STRING = 2
    FLOAT = 3
    ATTRIBUTE_TYPES_FIELDS = (
        (INTEGER, "integer"),
        (STRING, 'string'),
        (FLOAT, "float")
    )
    title = models.CharField(max_length=32)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='attributes')
    attribute_type = models.PositiveSmallIntegerField(default=INTEGER, choices=ATTRIBUTE_TYPES_FIELDS)

    def __str__(self):
        return self.title


class Brand(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    upc = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=32)
    desc = models.TextField(blank=True)

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products_cat')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='product_brand')

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ('user_score_permission', "user has score permission")
        ]


class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_val')
    value = models.CharField(max_length=48)
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE, related_name='productattribute_val')
