from django.db import models
from shop.models import Product 


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Cart {self.id}" 
    
    def get_total_price(self):
        return sum(cart_item.get_total_price() for cart_item in self.cart_items.all()) 


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=0)
    
    def get_total_price(self):
        price = int(self.product.price)
        quantity = int(self.quantity)
        return price * quantity

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
