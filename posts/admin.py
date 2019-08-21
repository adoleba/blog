from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'status', 'author')
    list_filter = ('status',)
    search_fields = ('title', 'body')
    ordering = ['published']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)

