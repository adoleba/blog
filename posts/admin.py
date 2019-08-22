from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'status', 'author')
    list_filter = ('status',)
    search_fields = ('title', 'body')
    ordering = ['-published']
    prepopulated_fields = {'slug': ('title',)}

    def get_exclude(self, request, obj=None):
        excluded = super().get_exclude(request, obj) or []
        if not request.user.is_superuser:
            return excluded + ['author']
        return excluded

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


admin.site.register(Post, PostAdmin)

