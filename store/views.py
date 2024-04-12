from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from .models import *
from .serializers import CategorySerializer,ProductSerializer,ImageProductSerializer,OfferSerializer,ReviewSerializer,ColorSerializer,SizeSerializer

# Create your views here.

class CategoryVIew(viewsets.ModelViewSet):
    queryset  = Category.objects.all()
    serializer_class = CategorySerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields  = ['name','description','category__name']

    @action(detail=True,methods=['GET'])
    def slug_product(self,request,id=None,slug=None):
        try:
            product = Product.objects.get(category__id=id,slug=slug)
            serializer = ProductSerializer(product)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
           message = {
               'message':'product not found'
           }
           return Response(message,status=status.HTTP_400_BAD_REQUEST) 
    @action(detail=True,methods=['GET'])
    def search_by_category(self,request,id=None):
        try:
            product = Product.objects.filter(category__id=id)
            serializer = ProductSerializer(product,many=True)
            json = {
                'number of product' : f'{len(product)} Products',
                'result'  : serializer.data
            }  
            return Response(json,status=status.HTTP_200_OK)
        except:
            json = {
                'message' : 'Product Not Found'
            }        
            return Response(json,status=status.HTTP_200_OK)
    
class ImageProductView(viewsets.ModelViewSet):
    queryset = ImageProduct.objects.all()
    serializer_class = ImageProductSerializer

class ColorView(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class SizeView(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class OfferView(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

