from django.contrib.auth import get_user_model
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer


User = get_user_model()


user_detail_url = HyperlinkedIdentityField(
    view_name='users-api:detail',
    lookup_field='username'
)


class UserListSerializer(ModelSerializer):
    url = user_detail_url

    class Meta:
        model = User
        fields = ['username', 'url']


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]
