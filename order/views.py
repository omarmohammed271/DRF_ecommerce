from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from store.models import Product
from .models import Order,OrderProduct,OrderComplete
from cart.models import CartItem
from .serializers import OrderProductSerializer,OrderSerializer,OrderCompleteSerializer
# Create your views here.

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def make_order(request,address2=None):
    user = request.user
    email = user.email
    if request.method=='POST':    
        f_name = request.data['f_name']
        l_name = request.data['l_name']
        phone = request.data['phone']
        address1 = request.data['address1']
        address2 = request.data.get('address2', '')
        city = request.data['city']
        try:
            order = Order.objects.get(user=user)
            order.f_name=f_name
            order.l_name=l_name
            order.email=email
            order.phone = phone
            order.address1=address1
            if address2:
                order.address2=address2
            order.city = city
            order.save()
            serializer = OrderSerializer(order)
            data = {
                'message' : 'Person Updated',
                'result' : serializer.data,
            }    
            return Response(data,status=status.HTTP_202_ACCEPTED)

        except:
            order = Order.objects.create(
                user=user,email=email,f_name=f_name,
                l_name=l_name,phone=phone,address1=address1,
                address2=address2,city=city 
                )
            serializer = OrderSerializer(order)
            data = {
                'message' : 'Person Created',
                'result' : serializer.data,
            }    
            return Response(data,status=status.HTTP_201_CREATED)
    elif request.method=='GET':
        order = Order.objects.filter(user=user)
        serializer=OrderSerializer(order,many=True)
        data = {
                'message' : 'List All Orders',
                'result' : serializer.data,
            }    
        return Response(data,status=status.HTTP_202_ACCEPTED)



@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def place_order(request):
    user = request.user
    if request.method == 'GET':
        order_product = OrderProduct.objects.filter(user=user)
        serializer = OrderProductSerializer(order_product,many=True)
        data = {
                'message' : 'List All user orders',
                'result' : serializer.data,
            }    
        return Response(data,status=status.HTTP_200_OK)
    
    elif request.method=='POST':
        order = Order.objects.get(user=user)
        items = CartItem.objects.filter(user=user)
        for item in items:
            order_product=OrderProduct()
            order_product.order_id = order.id
            order_product.user = user
            order_product.product = item.product
            order_product.quantity=item.quantity
            order_product.product_price=item.product.price
            order_product.ordered = True
            order_product.order_notes = f'color is : {item.color}  and size is : {item.size}'
            order_product.save()
            product = Product.objects.get(id=item.product_id)
            product.stock -= item.quantity
            product.save()
        CartItem.objects.filter(user=user).delete()
        data = {
                'message' : 'Place Order Success',
                
            }    
        return Response(data,status=status.HTTP_200_OK)   

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def order_complete(request):
    user=request.user
    if request.method=='GET':
        orders=OrderComplete.objects.filter(user=user)
        serializer = OrderCompleteSerializer(orders,many=True)
        data = {
                'message' : 'List All  orders completed',
                'result' : serializer.data,
            }    
        return Response(data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        products = []
        order = Order.objects.get(user=user)
        order_products = OrderProduct.objects.filter(user=user)
        
        for product in order_products:
            productname = product.product.name
            quantity = product.quantity
            price = product.product_price
            subtotal = product.sub_total
            products.append({
                'product': productname,
                'quantity': quantity,
                'price': price,
                'sub total': subtotal
            })
        
        order_product = OrderProduct.objects.get(user=user, product__name=products[0]['product'])
        
        orders = OrderComplete.objects.create(
            user=user,
            order=order,
            products=products,
            total_price=order_product.total
        )
        
        serializer = OrderCompleteSerializer(orders)
        
        data = {
            'message': 'Order completed successfully',
            'result': serializer.data
        }
        
        return Response(data, status=status.HTTP_200_OK)  






    



