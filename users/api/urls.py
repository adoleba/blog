from django.urls import path


from users.api.views import UserListAPIView, UserDetailAPIView
app_name = 'users'

urlpatterns = [
    path('', UserListAPIView.as_view(), name='list'),
    path('<username>/', UserDetailAPIView.as_view(), name='detail')
    ]
