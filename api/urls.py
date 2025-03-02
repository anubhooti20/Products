from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductAPIView
from .views import LoginPageView, ProductsPageView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductAPIView.as_view(), name='product-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("login/", LoginPageView.as_view(), name="login"),
    path("products/", ProductsPageView.as_view(), name="products"),
]
