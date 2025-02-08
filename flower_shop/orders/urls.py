from django.urls import path
from . import views


app_name = 'orders'
# urlpatterns = [
#     path('cart/<int:cart_id>/', views.CartDetailView.as_view(), name='cart_detail'),
#     path('cart/<int:cart_id>/add/<int:product_id>/', views.AddToCartView.as_view(), name='add_to_cart'),
#     path('cart/<int:cart_id>/remove/<int:product_id>/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
# ]

# urlpatterns = [
#     path('cart/<int:cart_id>/', views.CartDetailView.as_view(), name='cart_detail'),
#     path('cart/add/', views.AddToCartView.as_view(), name='add_to_cart'),
#     path('cart/remove/<int:product_id>/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
# ]


urlpatterns = [
    path('cart/', views.CartDetailView.as_view(), name='cart_detail'),
    path('cart/add/<int:product_id>/', views.CartAddView.as_view(), name='cart_add'),
    path('cart/remove/<int:product_id>/', views.CartRemoveView.as_view(), name='cart_remove'),
]