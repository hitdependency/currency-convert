import rest_framework.serializers as serializers

from django.contrib.auth.models import User


class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'subscriptions'
        )


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
        )

class UserAddSubscription(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'subscriptions',
        )