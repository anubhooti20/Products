from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')  # Using Meta class feature

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'created_at', 'category', 'category_name']
