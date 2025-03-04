from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductAPIView,RegisterAPIView,LoginAPIViewTest
from .views import ProductsPageView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('register/',RegisterAPIView.as_view(), name='register'),
    path('login/',LoginAPIViewTest.as_view(),name='login'),
    path('', include(router.urls)),
    path('products/', ProductAPIView.as_view(), name='products'),
    # path('products/<int:pk>/', ProductAPIView.as_view(), name='product-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path("login/", LoginPageView.as_view(), name="login"),
    path("products_page/", ProductsPageView.as_view(), name="products-page"),
]
