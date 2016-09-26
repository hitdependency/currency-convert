from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SubscriptionCreation
from .models import Subscription


class SubscriptionsView(GenericAPIView):
    serializer_class = SubscriptionCreation
    queryset = Subscription.objects.get_queryset()

    def get(self, request, *args, **kwargs):
        data = self.get_queryset().data
        return Response(data=data)

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = SubscriptionCreation(data=data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
           Subscription.objects.create(**serializer.validated_data)
           return Response(status=status.HTTP_201_CREATED)

