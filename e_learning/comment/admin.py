from django.contrib import admin
from comment.models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content']
    ordering = ['content']

admin.site.register(Comment,CommentAdmin)