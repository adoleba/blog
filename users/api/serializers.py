from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer, EmailField, ValidationError


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


class UserCreateUpdateDestroySerializer(ModelSerializer):
    email = EmailField(label='Email')
    email2 = EmailField(label='Confirm Email')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'email2',
            'password',
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def validate_email(self, value):
        data = self.get_initial()
        email1 = data.get('email2')
        email2 = value
        if email1 != email2:
            raise ValidationError('Emails must match')

        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
            raise ValidationError('This user has already registered')

        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get('email')
        email2 = value
        if email1 != email2:
            raise ValidationError('Emails must match')
        return value

    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(username=username, email=email, first_name=first_name, last_name=last_name, is_staff=True)
        group = Group.objects.get(name='authors')
        user_obj.save()
        user_obj.groups.add(group)
        user_obj.set_password(password)
        user_obj.save()

        return validated_data
