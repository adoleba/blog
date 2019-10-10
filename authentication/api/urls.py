from django.urls import path

from authentication.api.views import UserLoginAPIView

app_name = 'comments'

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='login'),
    ]
