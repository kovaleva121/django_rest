from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from users.apps import UsersConfig
from .views import  UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView
from users.views import PaymentsListApiView, PaymentsCreateApiView, PaymentsUpdateApiView, PaymentsRetrieveApiView, \
    PaymentsDestroyApiView, UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('payment/', PaymentsListApiView.as_view(), name='payment_list'),
    path('payment/<int:pk>/', PaymentsRetrieveApiView.as_view(), name='payment_retrieve'),
    path('payment/create/', PaymentsCreateApiView.as_view(), name='payment_create'),
    path('payment/<int:pk>/update/', PaymentsUpdateApiView.as_view(), name='payment_update'),
    path('payment/<int:pk>/delete/', PaymentsDestroyApiView.as_view(), name='payment_delete'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', UserListAPIView.as_view(), name='user_list'),
    path('<int:pk>/detail/', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('<int:pk>/update/', UserUpdateAPIView.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserRetrieveAPIView.as_view(), name='user_delete'),
]
