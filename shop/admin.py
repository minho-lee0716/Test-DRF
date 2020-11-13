from django.contrib import admin
from .models import (
    Product,
    Tag,
    ProductOption
)

admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(ProductOption)
