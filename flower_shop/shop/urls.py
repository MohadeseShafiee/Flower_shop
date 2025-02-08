from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
]