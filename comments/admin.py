from django.contrib import admin

from comments.models import PostComment


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'email', 'post', 'created')
    list_filter = ('post', 'created')
    search_fields = ('name', 'email', 'body')
    ordering = ('-created',)


admin.site.register(PostComment, PostCommentAdmin)
