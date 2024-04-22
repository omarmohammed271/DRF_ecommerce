from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import Account
from .serializers import UserSerializer
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(requets):
    if requets.method == 'POST':
        email = requets.data.get('email')
        password = requets.data.get('password')
        
        user = authenticate(email=email,password=password)
        if user:
            token,created = Token.objects.get_or_create(user=user)
            data = {
                'message' : 'login Success',
                'result' : token.key
            }
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
      
def logout_view(request):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == "POST":
        email = request.data.get('email')
        username = email.split('@')[0]
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        user = Account.objects.filter(email=email).first()
        if user:
            return Response({'error': 'User with that email already registered'}, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            new_password =Account.objects.make_random_password()
            user = Account.objects.create_user(
                email=email,first_name=first_name,last_name=last_name,username=username)
            user.set_password(new_password)
            user.save()
            # Send email with new password
            send_mail(
                'Password Reset',
                f'Your new password is: {new_password} \n for reset password go to http://127.0.0.1:8000/accounts/new_password/',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return Response({'message': 'Signup successful. Check your email for the new password.'}, status=status.HTTP_201_CREATED)
        
@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password(request):
     if request.method=='POST':
        email = request.data.get('email')
        user = Account.objects.filter(email=email).first()
        if user:
             #Generate random password and send it in his email
            new_password =Account.objects.make_random_password()
            user.set_password(new_password)
            user.save()
            # Send email with new password
            send_mail(
                'Password Reset',
                f'Your new password is: {new_password}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return Response({'message': 'Password reset successful. Check your email for the new password.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User with that email not found'}, status=status.HTTP_400_BAD_REQUEST)
                
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def new_password(request):
    if request.method=='POST':
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        if password1==password2:
              user = Account.objects.filter(email=request.user.email).first()
              user.set_password(password1)
              user.save()
              return Response({'message': 'Password reset successful.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'password and confirm password are not same'}, status=status.HTTP_400_BAD_REQUEST)


