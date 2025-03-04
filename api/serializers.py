from rest_framework import serializers
from .models import Product, Category
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')  # Using Meta class feature

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'created_at', 'category', 'category_name']
        
class RegisterSerializer(serializers.ModelSerializer):
    email= serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2 = serializers.CharField(write_only=True,required=True)
    
    class Meta:
        model=User
        fields=['username','email','password','password2']
        
    def validate(self,attrs):
        if attrs['password']!= attrs['password2']:
            raise serializers.ValidationError({'password':"Passwords dont match."})
        return attrs
    
    def create(self,validated_data):
        validated_data.pop('password2')
        user= User.objects.create_user(**validated_data)
        return user
    