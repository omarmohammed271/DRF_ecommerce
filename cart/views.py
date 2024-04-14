from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets,status
from store.models import Product
from .models import CartItem
from .serializers import CartItemSerializer
# Create your views here.

class CartItemViewset(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    
    def create(self, request, *args, **kwargs):
        response={
            'message':'Created from here Not allowed'
        }
        return Response(response,status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        response={
            'message':'Updated from here Not allowed'
        }
        return Response(response,status=status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        response={
            'message':'Retireve from here Not allowed'
        }
        return Response(response,status=status.HTTP_200_OK)
    def destroy(self, request, *args, **kwargs):
        response={
            'message':'Deleted from here Not allowed'
        }
        return Response(response,status=status.HTTP_200_OK)