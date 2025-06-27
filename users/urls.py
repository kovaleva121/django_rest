from django.urls import path
from users.apps import UsersConfig

from users.views import PaymentsListApiView, PaymentsCreateApiView, PaymentsUpdateApiView, PaymentsRetrieveApiView, \
    PaymentsDestroyApiView

app_name = UsersConfig.name

urlpatterns = [
    path('payment/', PaymentsListApiView.as_view(), name='payment_list'),
    path('payment/<int:pk>/', PaymentsRetrieveApiView.as_view(), name='payment_retrieve'),
    path('payment/create/', PaymentsCreateApiView.as_view(), name='payment_create'),
    path('payment/<int:pk>/update/', PaymentsUpdateApiView.as_view(), name='payment_update'),
    path('payment/<int:pk>/delete/', PaymentsDestroyApiView.as_view(), name='payment_delete')
]
