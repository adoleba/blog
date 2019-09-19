from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView

from users.api.serializers import UserListSerializer

User = get_user_model()


class UserListAPIView(ListAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = User.objects.all()
        return queryset_list
