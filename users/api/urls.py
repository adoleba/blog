from django.urls import path


from users.api.views import UserListAPIView
app_name = 'users'

urlpatterns = [
    path('', UserListAPIView.as_view(), name='list')
    ]
