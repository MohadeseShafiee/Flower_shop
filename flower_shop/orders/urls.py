from django.urls import path, include
from . import views


app_name = 'orders'
urlpatterns = [
    path('cart/', views.CartDetailView.as_view(), name='cart_detail'),
    path('cart/add/', views.CartAddView.as_view(), name='cart_add'),
    path('cart/remove/<int:product_id>/', views.CartRemoveView.as_view(), name='cart_remove'),
    path('cart/clear_session/', views.ClearSessionView.as_view(), name='clear_session'),
    path('cart/debug/',views.Debug.as_view(), name='debug'),
    path('api/admin/', views.OrderListView.as_view(), name='admin_orders'),
    path('api/admin/update/<int:pk>/', views.OrderUpdateView.as_view(), name='admin_update'),
    path('admin/reports/', views.AdminReportView.as_view(), name='admin_reports'),
]