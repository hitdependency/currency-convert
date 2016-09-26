from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .serializers import (
    UserViewSerializer, UserCreateSerializer
)

class UsersView(GenericAPIView):
    serializer_class = UserCreateSerializer

    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        data = request.data

        if request.user.is_authenticated():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = UserCreateSerializer(data=data, context={'request':request})

        if serializer.is_valid(raise_exception=True):
            User.objects.create(**serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class UserDetailView(GenericAPIView):
    serializer_class = UserViewSerializer

    def get_object(self):
        return get_object_or_404(User, )

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['id'])
        data = UserViewSerializer(user).data
        return Response(data=data)