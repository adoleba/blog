from django.contrib import admin

from users.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(admin.ModelAdmin):
    model = User

    #def get_fieldsets(self, request, obj=None):
        #fieldsets = list(super().get_fieldsets(request, obj))
        #if request.user.is_superuser:
            #fieldsets.append(
                #('Permissions', {
                    #'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
                #}))
        #return fieldsets

    #fieldsets = (
        #(None, {'fields': ('username', 'password')}),
        #('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
    #)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(username=request.user)


admin.site.register(User, UserAdmin)
