from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view 

urlpatterns = [  

    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('orders/', include('orders.urls')),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]