from django.urls import path, include
from .views      import testAPI

urlpatterns = [
    path('/test', testAPI),
]
