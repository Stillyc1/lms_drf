from django.contrib import admin

from lms.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Отображает модели пользователей в админке"""

    list_display = (
        "id",
        "title",
        "owner",
    )
    list_filter = (
        "title",
        "owner",
    )
    search_fields = ("id", "title", "owner")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """Отображает модели пользователей в админке"""

    list_display = (
        "id",
        "title",
        "course",
        "owner",
    )
    list_filter = (
        "title",
        "course",
        "owner"
    )
    search_fields = ("id", "title", "course", "owner",)
