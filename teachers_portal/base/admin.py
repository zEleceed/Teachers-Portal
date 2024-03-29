from django.contrib import admin
from .models import Classroom, Student, Comment


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0


class StudentAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine
    ]
    list_display = [
        "name",
    ]


admin.site.register(Classroom)
admin.site.register(Student, StudentAdmin)
admin.site.register(Comment)
