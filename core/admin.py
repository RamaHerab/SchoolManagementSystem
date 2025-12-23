from django.contrib import admin
from .models import Student, Teacher, Course, Classroom, Grade

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_id', 'date_of_birth')
    search_fields = ('user__first_name', 'user__last_name', 'student_id')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'teacher_id', 'department')
    search_fields = ('user__first_name', 'user__last_name', 'teacher_id')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'credits')
    search_fields = ('name', 'code')

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'location')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'grade', 'semester')
    list_filter = ('semester', 'course')
    search_fields = ('student__user__first_name', 'student__user__last_name')