from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
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
          serializer = UserSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               data={
                    'message' : 'registeration Successfully',
                    'result' : serializer.data
               }
               return Response(data,status=status.HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     

# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ResetPasswordView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         user = User.objects.filter(email=email).first()
        
#         if user:
#             # Generate a new password
#             new_password = User.objects.make_random_password()
#             user.set_password(new_password)
#             user.save()
            
#             # Send email with new password
#             send_mail(
#                 'Password Reset',
#                 f'Your new password is: {new_password}',
#                 settings.EMAIL_HOST_USER,
#                 [email],
#                 fail_silently=False,
#             )
            
#             return Response({'message': 'Password reset successful. Check your email for the new password.'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'User with that email not found'}, status=status.HTTP_400_BAD_REQUEST)

