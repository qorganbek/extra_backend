"""shop_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import JsonResponse, HttpResponse
from django.urls import path
from api.views import ProductAPIView
from api.models import Product
from api.views import all_products, all_categories, get_product, main_page, get_category, get_category_product

urlpatterns = [
    path('', main_page),
    path('admin/', admin.site.urls),
    path('api/categories/', all_categories),
    path('api/products/', all_products),
    path('api/products/<id>/', get_product),
    path('api/categories/<id>/', get_category),
    path('api/categories/<id>/products/', get_category_product),
]
