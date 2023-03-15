from django.shortcuts import render
from rest_framework.response import Response

from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
# Create your views here.


@api_view(['Get'])
def api_overview(request):
    api_urls = {
        'List': '/product-list',
        'Create': '/product-create',
        'Detail': '/product-detail/<int:id>',
        'Update': '/product-update/<int:id>',
        'Delete': '/product-delete/<int:id>',
    }
    return Response(api_urls)


# List View
@api_view(['Get'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# Create
@api_view(['Post'])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Single View
@api_view(['Get'])
def product_detail(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)


# Update
@api_view(['Post'])
def product_update(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=products, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Delete
@api_view(['Delete'])
def product_delete(request, pk):
    products = Product.objects.get(id=pk)
    products.delete()
    return Response('PRODUCT DELETED SUCCESSFULLY')
