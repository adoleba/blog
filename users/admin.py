from django.contrib import admin
from django.contrib.auth.models import User
from users.models import UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserProfileAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
