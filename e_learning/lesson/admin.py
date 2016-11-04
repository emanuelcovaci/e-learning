from django.contrib import admin
from lesson.models import Lesson

# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['title']

admin.site.register(Lesson, LessonAdmin)
