from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryListView(APIView):
    def get(self, request):
        category = Category.objects.all()
        ser_class = CategorySerializer(instance=category, many=True)
        return Response(data=ser_class.data)
    

class ProductListView(APIView):
    def get(self, request):
        product = Product.objects.all().order_by('id')
        ser_class = ProductSerializer(instance=product, many=True)
        return Response(data=ser_class.data)