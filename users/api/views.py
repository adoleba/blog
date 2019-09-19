from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveAPIView

from users.api.serializers import UserListSerializer, UserDetailSerializer

User = get_user_model()


class UserListAPIView(ListAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = User.objects.all()
        return queryset_list


class UserDetailAPIView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
