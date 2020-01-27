from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.authentication import BaseAuthentication, SessionAuthentication

from authentication.api.serializers import UserLoginSerializer


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request):
        user = {}
        user['username'] = request.data.get('username')
        user['email'] = request.data.get('email')
        user['password'] = request.data.get('password')
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=HTTP_200_OK)
