from django.contrib import admin
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    raw_id_fields = ('product',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'paid')
    list_filter = ('paid', 'created_at')
    inlines = (CartItemInline,)


@admin.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')