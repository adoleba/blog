from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'status', 'author')
    list_filter = ('status',)
    search_fields = ('title', 'body')
    ordering = ['published']
    prepopulated_fields = {'slug': ('title',)}
    exclude = ['author', ]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


admin.site.register(Post, PostAdmin)

