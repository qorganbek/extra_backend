from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
# from templates import 'index.html'
from api.models import Product, Category
from api.serializers import ProductSerializer


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def all_products(request):
    all_product = Product.objects.all()
    product = [{
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'number': p.number,
        'is_active': p.is_active,
    } for p in all_product
    ]
    return JsonResponse(product, safe=False)


def all_categories(request):
    category = Category.objects.all()
    json_file = [{'name': c.name} for c in category]
    return JsonResponse(json_file, safe=False)


def get_product(request, *args, **kwargs):
    product_id = int(kwargs["id"])
    products = Product.objects.get(id=product_id)
    info_product = [
        {
            'id': products.id,
            'name': products.name,
            'price': products.price,
            'number': products.number,
            'is_active': products.is_active,
        }
    ]

    return JsonResponse(info_product, safe=False)


def main_page(request):
    return render(request, 'index.html')


def get_category(request, *args, **kwargs):
    category_id = int(kwargs["id"])
    category = Category.objects.get(id=category_id)
    category_info = [{
        'name': category.name,
    }]
    return JsonResponse(category_info, safe=False)


def get_category_product(request, *args, **kwargs):
    p_id = int(kwargs["id"])
    products = Product.objects.get(id=p_id)
    info_product = [
        {
            'id': products.id,
            'name': products.name,
            'category': products.category.name,
            'price': products.price,
            'number': products.number,
            'is_active': products.is_active,
        }
    ]

    return JsonResponse(info_product, safe=False)
    
