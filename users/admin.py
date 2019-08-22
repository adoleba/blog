from django.contrib import admin
from django.contrib.auth.models import User, Permission
from django.forms import forms, ModelMultipleChoiceField

from users.models import UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserProfileAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

    def get_fieldsets(self, request, obj=None):
        fieldsets = list(super().get_fieldsets(request, obj))
        if request.user.is_superuser:
            fieldsets.append(
                ('Permissions', {
                    'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
                }))
        return fieldsets

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(username=request.user)




admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
