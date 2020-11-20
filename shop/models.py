from django.db import models

__all__ = [
    'Tag',
    'Product',
    'ProductOption'
]

class Tag(models.Model):
    name = models.CharField('태그명', unique=True, max_length=100)

    class Meta:
        db_table = 'tags'

    def __str__(self):
        return self.name


class Product(models.Model):
    name    = models.CharField('상품명', max_length=100)
    tag_set = models.ManyToManyField(Tag, blank=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name


class ProductOption(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name       = '상품',
        related_name       = 'option_set',
        related_query_name = 'option',
        on_delete          = models.CASCADE
    )
    name  = models.CharField('옵션명', max_length=100)
    price = models.IntegerField('가격')

    class Meta:
        db_table = 'product_options'

    def __str__(self):
        return self.name
