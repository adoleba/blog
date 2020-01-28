from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser

from users.api.permissions import IsRequestUserOrAdminUser
from users.api.serializers import UserListSerializer, UserDetailSerializer, UserCreateUpdateDestroySerializer

User = get_user_model()


class UserListAPIView(ListAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = User.objects.all()
        return queryset_list


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = [IsRequestUserOrAdminUser]
    lookup_field = 'username'


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateDestroySerializer
    permission_classes = [IsAdminUser]
