from django.urls import path

from users.api.views import UserListAPIView, UserDetailAPIView, UserCreateAPIView

app_name = 'users'

urlpatterns = [
    path('', UserListAPIView.as_view(), name='list'),
    path('create/', UserCreateAPIView.as_view(), name='create'),
    path('<username>/', UserDetailAPIView.as_view(), name='detail')
    ]
