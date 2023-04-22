from rest_framework import serializers
from caffe.models import AdminUser, Product

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser 
        fields = ['id', 'username', 'password']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['id', 'category', 'price', 'origin_price', 'name', 'info', 'barcode', 'expire', 'big_size']