from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class LoginPageView(TemplateView):
    template_name = "login.html"

class ProductsPageView(LoginRequiredMixin, TemplateView):
    template_name = "products.html"


# Using APIView
class ProductAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk=None):
        if pk:
            try:
                product = Product.objects.get(pk=pk)
                serializer = ProductSerializer(product)
            except Product.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Using ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

