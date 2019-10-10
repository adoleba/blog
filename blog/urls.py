"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import HomCKEDITOR_RESTRICT_BY_USERe
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blog.views import error_404

urlpatterns = [
    path('', include('posts.urls')),
    path('user/', include('users.urls')),
    path('category/', include('categories.urls')),
    path('contact/', include('contact.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('api/', include("authentication.api.urls", namespace='login')),
    path('api/categories/', include("categories.api.urls", namespace='categories-api')),
    path('api/comments/', include("comments.api.urls", namespace='comments-api')),
    path('api/posts/', include("posts.api.urls", namespace='posts-api')),
    path('api/users/', include("users.api.urls", namespace='users-api')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = error_404
