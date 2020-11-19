from django.urls import path, include
from .views import (
    testAPI,
    create_product
)

urlpatterns = [
    path('/products', testAPI),
    path('/create_product', create_product),
]
