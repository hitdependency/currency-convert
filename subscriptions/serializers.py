import rest_framework.serializers as serializers


from subscriptions.models import Subscription

class SubscriptionCreation(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ('text',)
