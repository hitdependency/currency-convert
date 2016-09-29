from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import SubscriptionCreation, SubscriptionDetailedView
from .models import Subscription


class SubscriptionsView(GenericAPIView):
    serializer_class = SubscriptionCreation
    queryset = Subscription.objects.get_queryset()

    def get(self, request, *args, **kwargs):
        data = SubscriptionCreation(self.get_queryset(), many=True).data
        return Response(data=data)

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = SubscriptionCreation(data=data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
           Subscription.objects.create(**serializer.validated_data)
           return Response(status=status.HTTP_201_CREATED)

class SubscriptionsDetailView(GenericAPIView):
    serializer_class =  SubscriptionDetailedView

    def get(self, request, *args, **kwargs):
        currency = get_object_or_404(Subscription, id=kwargs['id'])
        data = SubscriptionDetailedView(currency).data
        return Response(data=data)

    def delete(self, request, *args, **kwargs):
        currency = get_object_or_404(Subscription, id=kwargs['id'])
        currency.delete()
        pass

