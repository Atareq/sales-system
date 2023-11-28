from rest_framework import serializers
from .models import CustomUser

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)  # Add this line to make username required
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
   

    class Meta:  
        model = CustomUser
        fields = ['username', 'password', 'phone_number', 'address', 'first_name', 'last_name', 'is_staff']

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)  
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:  
        model = CustomUser
        fields = ['username', 'password']
