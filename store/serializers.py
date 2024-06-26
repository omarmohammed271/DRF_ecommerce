from rest_framework import serializers
from .models import Category,Product,ImageProduct,Color,Size,Review,Offer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = '__all__'
class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=ImageProduct
        fields = '__all__'       
        
class ProductSerializer(serializers.ModelSerializer):
    images = ImageProductSerializer(many=True, read_only=True)

    class Meta:
        model=Product
        fields = 'name','images','category','slug','price','size','color','description','stock','is_available','updated_at','number_of_rating','avg'
        

        
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Size
        fields = 'name',
    

        
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Color
        fields = 'name',
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields = 'user','product','rating','comment'
        

        
class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model=Offer
        fields = 'product','discount_precentage','start_date','end_date','price_after'

        