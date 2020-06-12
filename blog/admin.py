from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, Comment


class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_date')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_date', 'active')
    list_filter = ('active', 'created_date')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

# bham2020
