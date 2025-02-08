from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartItemSerializer
from django.shortcuts import get_object_or_404
from .models import CartItem, Cart, Product




class CartDetailView(APIView):
    def get(self, request):
        cart = Cart(request)
        serializer_class = CartItemSerializer(cart)
        # serializer_class.data['total_price'] = 0
        return Response(serializer_class.data, status=status.HTTP_200_OK)


class CartAddView(APIView):
    def post(self, request, product_id):
        # product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        cart_id = request.data.get('cart_id', 1)
        cart_id = 3
        cart = get_object_or_404(Cart, id=cart_id)
        product = get_object_or_404(Product, id=product_id)
        cartitem = CartItem(product=product, quantity=quantity, cart=cart)
        cartitem.save()
        return Response({'message': 'محصول به سبد خرید اضافه شد!'}, status=status.HTTP_200_OK)

class CartRemoveView(APIView):
    def delete(self, request, product_id):
        cart = Cart(request)
        cart.remove(product_id)
        return Response({'message':'محصول از سبد خرید حذف شد!'}, status=status.HTTP_200_OK)



















# class CartDetailView(APIView):
#     # def get(self, request, cart_id):
#     #     cart = get_object_or_404(Cart, id=cart_id)
#     #     serializer_class = CartSerializer(cart)
#     #     return Response(data=serializer_class.data)

#     # def get(self, request, cart_id):
#     #     try:
#     #         cart = Cart.objects.get(id=cart_id)
#     #         serializer_class = CartSerializer(cart)
#     #         return Response(data=serializer_class.data)
#     #     except Cart.DoesNotExist:
#     #         return Response({"error":"سبد خرید پیدا نشد"}, status=status.HTTP_404_NOT_FOUND)
    
#     def get(self, request):
#         cart_id = request.session.get('cart_id')
#         if not cart_id:
#             return Response({"error":"سبد خرید پیدا نشد!"}, status=status.HTTP_404_NOT_FOUND)
        
#         try:
#             cart = Cart.objects.get(id=cart_id)
#             serializer_class = CartSerializer(cart)
#             return Response(serializer_class.data)
#         except Cart.DoesNotExist:
#             return Response({"error":"سبد خرید پیدا نشد!"}, status=status.HTTP_404_NOT_FOUND)


#     # def get(self, request):
#     #     print('session:', request.session.items())

#     #     cart_id = request.session.get('cart_id', None)
#     #     print('cart_id:', cart_id)

#     #     if cart_id is None:
#     #         return Response({'error':'هیچ کارت آیدی در سشن یافت نشد'}, status=status.HTTP_404_NOT_FOUND)
        
#     #     cart_exists = Cart.objects.filter(id=cart_id).exists()
#     #     print('cart_id', cart_exists)

#     #     if not cart_exists:
#     #         return Response({'error':'سبد خرید با این آیدی در دیتابیس نیست'}, status=status.HTTP_404_NOT_FOUND)
        
#     #     cart = Cart.objects.get(id=cart_id)
#     #     serializer = CartSerializer(cart)
#     #     return Response(serializer.data)


    

# class AddToCartView(APIView):
#     # def post(self, request, cart_id, product_id):
#     #     cart = get_object_or_404(Cart, id=cart_id)
#     #     product = get_object_or_404(Product, id=product_id)
#     #     cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#     #     if created:
#     #         cart_item.quantity = 1
#     #     else:
#     #         cart_item.quantity += 1
#     #     cart_item.save()
#     #     return Response({'message':'محصول به سبد خرید اضافه شد!'})
#     def post(self, request):
#         cart_id = request.session.get('cart_id')

#         if not cart_id:
#             cart = Cart.objects.create()
#             request.session['cart_id'] = cart.id
#         else:
#             cart = get_object_or_404(Cart, id=request.session['cart_id'])

#         product_id = request.data.get('product_id')
#         quantity = request.data.get('quantity', 1)
#         product = get_object_or_404(Product, id=product_id)
#         cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#         if not created:
#             cart_item.quantity += quantity
#         else:
#             cart_item.quantity = quantity
#         cart_item.save()

#         return Response({'message':'محصول با موفقیت به سبد خرید اضافه شد!'}, status=status.HTTP_200_OK)
    

# class RemoveFromCartView(APIView):
#     # def post(self, request, cart_id, product_id):
#     #     cart = get_object_or_404(Cart, id=cart_id)
#     #     cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
#     #     cart_item.delete()
#     #     return Response({'message':'محصول از سبد خرید حذف شد!'})



#     # def delete(self, request, product_id):
#     #     try:
#     #         cart_item = get_object_or_404(CartItem, product_id=product_id)
#     #         cart_item.delete()
#     #         return Response({'message':"محصول با موفقیت حذف شد!"})
#     #     except CartItem.DoesNotExist:
#     #         return Response({'error':"محصول مورد نظر در سبد خرید نیست!"}, status=status.HTTP_404_NOT_FOUND)


#     # def delete(self, request):  
#     #     cart_id = request.data.get('cart_id')  
#     #     product_id = request.data.get('product_id')  

#     #     try:  
#     #         cart = Cart.objects.get(id=cart_id)  
#     #         cart_item = CartItem.objects.get(cart=cart, product_id=product_id)  
#     #         cart_item.delete()  
#     #         return Response({'message': 'Item removed from cart.'}, status=status.HTTP_204_NO_CONTENT)  
#     #     except Cart.DoesNotExist:  
#     #         return Response({'error': 'Cart not found.'}, status=status.HTTP_404_NOT_FOUND)  
#     #     except CartItem.DoesNotExist:  
#     #         return Response({'error': 'Item not found in cart.'}, status=status.HTTP_404_NOT_FOUND) 

#     def delete(self, request, product_id):
#         cart_id = request.session.get('cart_id')
#         if not cart_id:
#             return Response({'error':'سید خریدی یافت نشد!'}, status=status.HTTP_404_NOT_FOUND)
        
#         cart = get_object_or_404(Cart, id=cart_id)
#         cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
#         cart_item.delete()
#         return Response({'message':'محصول با موفقیت از سبد خرید حذف شد!'}, status=status.HTTP_200_OK)