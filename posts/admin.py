from django.contrib import admin
from posts.models import PostCategory, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'status', 'author')
    list_filter = ('status',)
    search_fields = ('title', 'body')
    ordering = ['published']


admin.site.register(PostCategory)
admin.site.register(Post, PostAdmin)
