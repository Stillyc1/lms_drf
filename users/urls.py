from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, \
    UserDestroyAPIView, PaymentListAPIView, PaymentCreateAPIView, PaymentSessionRetrieveAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', UserListAPIView.as_view(), name='user-list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),

    path('payment_create/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
    path('payment/sessions/<int:pk>/', PaymentSessionRetrieveAPIView.as_view(), name="session-retrieve"),

    path('token/', TokenObtainPairView.as_view(permission_classes=[AllowAny]), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=[AllowAny]), name='token_refresh'),
]
