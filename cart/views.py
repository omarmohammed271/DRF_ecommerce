from django.shortcuts import render
from rest_framework.decorators import action,api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets,status
from store.models import Product
from .models import CartItem
from .serializers import CartItemSerializer
# Create your views here.
# with function Based View
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_cart(request,shipping=10):
    if request.method == 'GET':
        cart_items = CartItem.objects.filter(user=request.user)
        serializer = CartItemSerializer(cart_items,many=True)
        total_price = [item.total for item in cart_items][0]
        respnse = {
            'price before shipping' : total_price,
            'shipping' : shipping,
            'total price after shipping' : total_price+shipping,
            'result' : serializer.data,
        }
        return Response(respnse,status=status.HTTP_200_OK)



#another way with viewsets

# class CartItemViewset(viewsets.ModelViewSet):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = CartItem.objects.all()
#     serializer_class = CartItemSerializer

#     def list(self, request, *args, **kwargs):
#         shipping = 10
#         cart_items = CartItem.objects.filter(user=request.user)
#         serializer = CartItemSerializer(cart_items,many=True)
#         total_price = [item.total for item in cart_items][0]
#         respnse = {
#             'price before shipping' : total_price,
#             'shipping' : shipping,
#             'total price after shipping' : total_price+shipping,
#             'result' : serializer.data,
#         }
#         return Response(respnse,status=status.HTTP_200_OK)
    

#     def create(self, request, *args, **kwargs):
#         response={
#             'message':'Created from here Not allowed'
#         }
#         return Response(response,status=status.HTTP_200_OK)
    
#     def update(self, request, *args, **kwargs):
#         response={
#             'message':'Updated from here Not allowed'
#         }
#         return Response(response,status=status.HTTP_200_OK)
    
#     def retrieve(self, request, *args, **kwargs):
#         response={
#             'message':'Retireve from here Not allowed'
#         }
#         return Response(response,status=status.HTTP_200_OK)
#     def destroy(self, request, *args, **kwargs):
#         response={
#             'message':'Deleted from here Not allowed'
#         }
#         return Response(response,status=status.HTTP_200_OK)