from django.urls import path
from . import views



urlpatterns = [
    path('api/products/', views.ProductListView.as_view(), name='products'),
    path('api/categories/', views.CategoryListView.as_view(), name='categories'),
    path('api/admin/products/', views.ProductAdminView.as_view(), name='admin_products'),
    path('api/admin/categories/', views.CategoryAdminView.as_view(), name='admin_categories'),
    path('api/admin/products/<int:pk>/', views.ProductDetailAdminView.as_view(), name='admin_product_detail'),
    path('api/admin/categories/update/<int:pk>/', views.CategoryUpdateView.as_view(), name='admin_update_categories'),
]