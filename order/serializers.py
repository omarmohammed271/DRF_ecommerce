from rest_framework import serializers
from .models import Order,OrderProduct,OrderComplete

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','user','email','f_name','l_name','phone','address1','address2','city']

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['id','user','order','product','quantity','product_price']

class OrderCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderComplete
        fields = ['id','user','order','products','total_price','created_at']


