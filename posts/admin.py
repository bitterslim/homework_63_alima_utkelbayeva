from django.contrib import admin
from posts.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'description']
    ordering = ['-created_at']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment_text', 'post_id']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)