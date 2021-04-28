from school.models import ExamScore
from django.contrib import admin
from .models import *

# Register your models here.
class ExamAdmin(admin.ModelAdmin):
    list_display = ['subject',
                    'student_name',
                    'score']

    list_filter = ['subject']

admin.site.register(ExamScore, ExamAdmin)


# ใช้แสดงการแสดงผลหน้า Admin
class StudentAdmin(admin.ModelAdmin):
    list_display = ['level',
                    'student_id',
                    'student_name',
                    'student_tel']
    
    list_filter = ['level']

    list_editable = ['student_tel']

admin.site.register(AllStudent, StudentAdmin)

