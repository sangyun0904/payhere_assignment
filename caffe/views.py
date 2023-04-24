from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from caffe.models import Seller, Product
from caffe.serializers import SellerSerializer, ProductSerializer
from django.contrib.auth.models import User

# Create your views here.

@csrf_exempt
def seller_signup(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SellerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.create_user(data["username"], data["username"] + "@payhere.com", data["password"])
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def product_list(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def product_detail(request, pk):

    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)