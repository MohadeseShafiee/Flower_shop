import django_filters
from .models import Cart, Product
from django.db.models import Q

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Cart
        fields = {
            'paid': ['exact'],
            'created_at': ['gte', 'lte']
        }

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'price': ['exact', 'gte', 'lte'],
        }