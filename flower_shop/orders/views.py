from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartSerializer
from django.shortcuts import get_object_or_404
from .models import CartItem, Cart, Product


CART_SESSION_ID = 'cart'

class Debug(APIView):
    def get(self, request):
        return Response({'session':dict(request.session.items())})

class CartDetailView(APIView):
    def get(self, request):
        cart_id = request.session.get(CART_SESSION_ID)
        if not cart_id:
            cart = Cart.objects.create()
            request.session[CART_SESSION_ID] = cart.id
            request.session.modified = True
            return Response({'message':'سبد خرید وجود ندارد.'}, status=status.HTTP_404_NOT_FOUND)
        cart = get_object_or_404(Cart, id=cart_id)
        serializer_class = CartSerializer(cart)
        total_price = cart.get_total_price()
        return Response({'message':'سبد خرید با موفقیت پیدا شد', 'data':serializer_class.data, 'total_price':total_price}, status=status.HTTP_200_OK)

    def post(self, request):
        cart_id = request.session.get(CART_SESSION_ID)
        if not cart_id:
            cart = Cart.objects.create()
            request.session[CART_SESSION_ID] = cart.id
            request.session.modified = True
            return Response({'message':'سبد خرید ایجاد شد.', 'cart_id':cart.id}, status=status.HTTP_201_CREATED)
        return Response({'message':'سبد خرید از قبل وجود دارد.', 'cart_id':cart.id}, status=status.HTTP_200_OK)


class CartAddView(APIView):  
    def post(self, request):
        cart_id = request.session.get(CART_SESSION_ID)
        if not cart_id:
            cart = Cart.objects.create()
            request.session[CART_SESSION_ID] = request.session.mofified = True
            message = 'سبد خرید جدید ایجاد شد'
        else:
            cart = get_object_or_404(Cart, id=cart_id)
            message = 'سبد خرید از قبل وجود دارد'
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        cart_item = CartItem.objects.filter(cart=cart, product_id=product_id).first()
        if cart_item:
            cart_item.quantity += quantity
            cart_item.save()
            message = 'تعداد محصول به روز رسانی شد.'
        else:
            product = get_object_or_404(Product, id=product_id)
            cart_item = CartItem(cart=cart, product=product, quantity=quantity)
            cart_item.save()

        return Response({'message':message}, status=status.HTTP_200_OK)
        

class CartRemoveView(APIView):
    def delete(self, request, product_id):
        cart_id = request.session.get(CART_SESSION_ID)
        if not cart_id:
            return Response({'error':'سبد خرید وجود ندارد.'}, status=status.HTTP_404_NOT_FOUND)
        cart = get_object_or_404(Cart, id=cart_id)
        quantity_to_remove = int(request.data.get('quantity', 1))
        cart_item = CartItem.objects.filter(cart=cart, product_id=product_id).first()
        if not cart_item:
            return Response({'error':'محصول در سبد خرید وجود ندارد'}, status=status.HTTP_404_NOT_FOUND)
        if cart_item.quantity > quantity_to_remove:
            cart_item.quantity -= quantity_to_remove
            cart_item.save()
            message = f"{quantity_to_remove} عدد از محصول حذف شد {cart_item.product.name}"
        else:
            cart_item.delete()
            message = f"{cart_item.product.name}محصول از سبد خرید حذف شد"
        return Response({'message':message}, status=status.HTTP_200_OK)
    

class ClearSessionView(APIView):
    def post(self, request):
        request.session.flush()
        #request.session.modified = True
        return Response({"message": "Session deleted"}, status=status.HTTP_200_OK)