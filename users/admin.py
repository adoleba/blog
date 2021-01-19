from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    model = User
    exclude = ['password']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(username=request.user)


admin.site.register(User, UserAdmin)
