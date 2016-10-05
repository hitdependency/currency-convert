import rest_framework.serializers as serializers

from django.contrib.auth.models import User
from subscriptions.models import Subscription
from django.shortcuts import get_object_or_404


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

class UserAddSubscription(serializers.Serializer):
    class Meta:
        model = User
        fields = (
            'subscriptions',
        )

    def validate(self, attrs):
        # subscription = get_object_or_404(Subscription, id=attrs['id'])
        print('te:', attrs['subscriptions'])
        print('sd:', self)

        subscription = Subscription.objects.get(id=attrs['id'])

        print(subscription)
        print("TYT SELF:", self)
        # if :
        #     msg = 'TOO LONG'
        #     raise serializers.ValidationError(msg)
        return attrs