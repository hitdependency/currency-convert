from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.authtoken.models import Token

from .serializers import (
    UserViewSerializer, UserCreateSerializer, UserAddSubscription
)


class UsersView(GenericAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        data = request.data

        if request.user.is_authenticated():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = self.serializer_class(data=data, context={'request':request})
        if serializer.is_valid(raise_exception=True):
            User.objects.create(**serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class UserSubscriptionsControl(GenericAPIView):
    serializer_class = UserAddSubscription
    queryset = User.objects.get_queryset()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        user = get_object_or_404(User, id=kwargs['id'])

        if not request.user == user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


        if serializer.is_valid(raise_exception=True):
            user.subscriptions.add(*serializer.validated_data['subscriptions'])
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        user = get_object_or_404(User, id=kwargs['id'])

        if not request.auth is Token.objects.get(user=user).key:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid(raise_exception=True):
            user.subscriptions.remove(*serializer.validated_data['subscriptions'])
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class UserDetailView(GenericAPIView):
    serializer_class = UserViewSerializer

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User,id=kwargs['id'])
        data = self.serializer_class(user).data
        return Response(data=data)
