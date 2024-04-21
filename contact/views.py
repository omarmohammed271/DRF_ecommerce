from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.decorators import permission_classes,api_view,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def contact(request):
    if request.method == "POST":
        subject = request.data.get('subject')
        email = request.data.get('email').split(',')
        message = request.data.get('message')
        sender = settings.EMAIL_HOST_USER
        reciever = email
        send_mail(
            subject,
            message,
            sender,
            reciever,
            fail_silently=False,
        )

    return Response({'message':'message sended',},status=status.HTTP_200_OK)