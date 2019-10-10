from django.contrib.auth import get_user_model, authenticate
from django.db.models import Q
from rest_framework.serializers import ModelSerializer, CharField, EmailField, ValidationError
User = get_user_model()


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label='Email', required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise ValidationError('An email address is required to log in')

        if password is None:
            raise ValidationError('A password is required to log in')

        user = authenticate(username=email, password=password)

        if user is None:
            raise ValidationError('A user with this email and password was not found')

        if not user.is_active:
            raise ValidationError('This user has been deactivated')

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }
