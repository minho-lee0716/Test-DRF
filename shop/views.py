from rest_framework.response   import Response
from rest_framework.decorators import api_view

from .serializers import (
    ProductSerializer,
    TagSerializer,
    ProductOptionSerializer
)
from .models import (
    Product,
    Tag,
    ProductOption
)

@api_view(['GET'])
def testAPI(request):
    products = Product.objects.all()
    print(products)
    serializer = ProductSerializer(products, many=True)
    print(serializer)
    print('#####')
    print(serializer.data)
    return Response({'data':serializer.data})
