from rest_framework import serializers
from .models import Category,Product,ImageProduct,Color,Size,Review,Offer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = '__all__'
        
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = '__all__'
        exclude = 'id','user',

        
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Size
        fields = '__all__'
        exclude = 'id',

        
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Color
        fields = '__all__'
        exclude = 'id',

        
class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=ImageProduct
        fields = '__all__'
        exclude = 'id',

        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields = '__all__'
        

        
class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model=Offer
        fields = '__all__'

        