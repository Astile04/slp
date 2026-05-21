from django.contrib import admin
from . models import Course,Lesson,Enrollment


class CourseInline(admin.TabularInline):
    model=Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','instructor','level','status']
    list_filter = ['level','status']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CourseInline]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title','course','order','is_free']
    list_filter = ['is_free']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student','course','status','enrolled_at']
    list_filter = ['status']
