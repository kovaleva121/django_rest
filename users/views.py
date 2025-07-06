from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, \
    get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course
from users.models import Payments, User, Subscription
from users.serializers import PaymentsSerializer, UserSerializer, UserUpdateSerializer, SubscriptionSerializer


class PaymentsCreateApiView(CreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsListApiView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['payment_course', 'payment_lesson', 'payment_method']
    ordering_fields = ['payment_date']


class PaymentsUpdateApiView(UpdateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsRetrieveApiView(RetrieveAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsDestroyApiView(DestroyAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        print(user.password, 111)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user


class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user


class UserDestroyAPIView(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class SubscriptionApiView(APIView):
    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course_id')
        course_item = get_object_or_404(Course, id=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            return Response({"message": "подписка удалена"}, status=status.HTTP_200_OK)
        else:
            Subscription.objects.create(user=user, course=course_item)
            return Response({"message": "подписка добавлена"}, status=status.HTTP_201_CREATED)