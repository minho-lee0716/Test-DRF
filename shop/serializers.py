from rest_framework import serializers
from .models import (
    Product,
    Tag,
    ProductOption
)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = (
            'title',
        )

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'name',
            'tag_set'
        )

class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = (
            'name',
            'price',
            'product'
        )
