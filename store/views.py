from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
# Create your views here.

class CategoryVIew(viewsets.ModelViewSet):
    queryset  = Category.objects.all()
    serializer_class = CategorySerializer