from rest_framework.exceptions import PermissionDenied
from rest_framework.serializers import ModelSerializer

from users.models import Payments, User


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'city', 'password']
        read_only_fields = ['id']

class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'city']

    # def validate(self, attrs):
    #     if self.instance != self.context['request'].user:
    #         PermissionDenied('Вы не можете редактировать чужой профиль')
    #         return attrs
