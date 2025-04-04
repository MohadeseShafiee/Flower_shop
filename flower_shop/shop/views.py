from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from orders.filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 50
    

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


class ProductAdminView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    permission_classes = [permissions.IsAdminUser]
    pagination_class = ProductPagination
    #parser_classes = [MultiPartParser, FormParser]

class ProductDetailAdminView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]
    

class CategoryAdminView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]