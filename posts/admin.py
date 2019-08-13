from django.contrib import admin
from posts.models import PostCategory, Post


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(PostCategory, PostCategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'status', 'author')
    list_filter = ('status',)
    search_fields = ('title', 'body')
    ordering = ['published']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)

