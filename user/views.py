from django.contrib.auth import authenticate , get_user
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes ,authentication_classes
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout
from .models import CustomUser
from user.models import CustomUser
from .serializers import UserRegisterSerializer, UserLoginSerializer
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication


@permission_classes([IsAdminUser])
class UserRegistration(APIView):

    def post(self, request):
        serialized_register = UserRegisterSerializer(data=request.data)
        if serialized_register.is_valid():
            user = CustomUser.objects.create_user(username=request.data['username'], password=request.data['password'])
            login(request, user)  
            return Response({'message': 'User registered successfully', 'data': request.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serialized_register.errors, 'data': request.data}, status=status.HTTP_400_BAD_REQUEST)

class UserLogIn(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serialized_login = UserLoginSerializer(data=request.data)
        if serialized_login.is_valid():       
            user = authenticate(request, username=request.data['username'], password=request.data['password'])
            if user is not None:
                user.last_login = timezone.now()
                user.save()
                login(request, user)  # Log the user in
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key},  status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serialized_login.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogOut(APIView):

    def post(self, request):
        Token.objects.all().delete()

        return Response({'detail': 'You have been logged out.'}, status=status.HTTP_200_OK)