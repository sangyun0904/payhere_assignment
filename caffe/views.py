from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from caffe.models import Seller, Product
from caffe.serializers import SellerSerializer, ProductSerializer
from django.contrib.auth.models import User
from jamo import h2j, j2hcj
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class SellerSignup(APIView):

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = SellerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.create_user(data["username"], data["username"] + "@payhere.com", data["password"])
            return JsonResponse({"meta":{"code":201, "message":"ok"}, "data":serializer.data}, status=201)
        return JsonResponse({"meta":{"code":400, "message":serializer.errors}, "data":None}, status=400)

class ProductList(APIView):

    permission_classes=[IsAuthenticated]

    def get_seller_id(self, user):
        seller = Seller.objects.get(username=user)
        return seller.id

    def get(self, request, page):
        seller_id = self.get_seller_id(request.user)
        products = Product.objects.all().filter(seller_id=seller_id)
        serializer = ProductSerializer(products, many=True)
        data_list = list(serializer.data)[page*10:(page+1)*10]
        return JsonResponse({"meta":{"code":200, "message":"ok"}, "data":{"products":data_list}}, safe=False)

class ProductPost(APIView):

    permission_classes=[IsAuthenticated]

    def get_seller_id(self, user):
        seller = Seller.objects.get(username=user)
        return seller.id

    def post(self, request):
        data = JSONParser().parse(request)
        data["seller"] = self.get_seller_id(request.user)
        print(type(data), data)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"meta":{"code":201, "message":"ok"}, "data":serializer.data}, status=201)
        return JsonResponse({"meta":{"code":400, "message":serializer.errors}, "data":None}, status=400)

class ProductDetail(APIView):

    permission_classes=[IsAuthenticated]

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response({"meta":{"code":200, "message":"ok"}, "data":{"product":serializer.data}}, status=200)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"meta":{"code":201, "message":"ok"}, "data":{"product":serializer.data}}, status=201)
        return Response({"meta":{"code":201, "message":serializer.errors}, "data":None}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response({"meta":{"code":204, "message":"ok"}, "data":None}, status=status.HTTP_204_NO_CONTENT)

class ProductSearch(APIView):

    permission_classes=[IsAuthenticated]

    def get_seller_id(self, user):
        seller = Seller.objects.get(username=user)
        return seller.id

    def get(self, request, page, search):
        seller_id = self.get_seller_id(request.user)
        products = Product.objects.all().filter(seller_id=seller_id)
        serializer = ProductSerializer(products, many=True)
        data = list(serializer.data)
        result = []
        for i in data:
            if search_engine(i["name"], search):
                result.append(i)

        return JsonResponse({"meta":{"code":200, "message":"ok"}, "data":{"products":result}}, safe=False)


def search_engine(productName, keyword):
    if keyword == "":
        return True

    words = list(productName.split())
    chosungs = []
    for word in words:
        temp = []
        for i in word:
            h = h2j(i)
            imf = j2hcj(h)
            temp.append(imf[0])
        chosungs.append("".join(temp))
    for word in words:
        if keyword in word:
            return True
    for chosung in chosungs:
        if keyword in chosung:
            return True
    return False
