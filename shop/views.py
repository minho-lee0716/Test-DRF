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
    print('##########')
    products = Product.objects.all()
    print(type(products))
    serializer = ProductSerializer(products, many=True)
    print(type(serializer))
    print('##########')
    print(serializer.data)
    return Response({'data':serializer.data})

@api_view(['POST'])
def create_product(request):
    data = json.loads(request.body)
    print(data)
    return 0
