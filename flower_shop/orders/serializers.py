from rest_framework import serializers
from .models import Cart, CartItem
from shop.serializers import ProductSerializer


class CartItemSerializer(serializers.Serializer):
    product = ProductSerializer(read_only=True)
    quantity = serializers.IntegerField()
    total_price = serializers.IntegerField()
        

# class CartSerializer(serializers.ModelSerializer):
#     cart_items = CartItemSerializer(many=True)
#     total_price = serializers.IntegerField()