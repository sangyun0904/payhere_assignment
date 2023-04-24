from rest_framework import serializers
from caffe.models import Seller, Product

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller 
        fields = ['id', 'username', 'password']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['id', 'category', 'price', 'origin_price', 'name', 'info', 'barcode', 'expire', 'big_size']