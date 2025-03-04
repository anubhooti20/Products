# from tokenize import Token

from rest_framework.authtoken.models import Token

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from rest_framework import generics,status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect


# def get_token_for_user(user):
#     refresh = RefreshToken.for_user(user)
#     return {
#         'refresh':str(refresh),
#         'access':str(refresh.access_token),
#     }
    
class RegisterAPIView(generics.CreateAPIView):
    queryset= User.objects.all()
    permission_classes= (AllowAny,)
    serializer_class= RegisterSerializer
    
    def create(self,request,*args,**kwargs):
        response= super().create(request,*args,**kwargs)
        return redirect('/api/login/')
    
class LoginAPIViewTest(APIView):
    permission_classes= (AllowAny,)
    
    def post(self,request):
        username= request.data.get('username')
        password= request.data.get('password')
        
        if not username or not password:
            return Response({'error':'Username and password are required'},status=status.HTTP_400_BAD_REQUEST)
        user= authenticate(username =username,password= password)
        if user:
            # Generate or retrieve an authentication token
            
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'message': 'Login Successful',
                'redirect_url':'/accounts/products/'
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
# class LoginPageView(TemplateView):
#     template_name = "login.html"

class ProductsPageView(LoginRequiredMixin, TemplateView):
    template_name = "products.html"


# Using APIView
class ProductAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request ,*args, **kwargs):
        pk = request.query_params.get("pk")
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
    def post(self, request,*args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request,*args, **kwargs):
        pk = request.query_params.get("pk")
        if not pk:
            return Response(data="pk is mandatory query parameter", status=status.HTTP_400_BAD_REQUEST)
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,*args, **kwargs):
        pk = request.query_params.get("pk")
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



















