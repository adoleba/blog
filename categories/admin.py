from django.contrib import admin

from categories.models import Category


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, PostCategoryAdmin)
