from django.db import models
from django.db.models.base import Model
from django.utils.translation import deactivate_all

# Create your models here.
class ExamScore(models.Model):
    allSubject =   (('คณิตศาสตร์', 'คณิตศาสตร์'),
                    ('วิทยาศาสตร์', 'วิทยาศาสตร์'),
                    ('ศิลปะ', 'ศิลปะ'),
                    ('ภาษาอังกฤษ', 'ภาษาอังกฤษ'),
                    ('ฟิสิกส์', 'ฟิสิกส์'),
                    ('ชีววิทยา', 'ชีววิทยา'))

    subject = models.CharField(max_length=200, choices=allSubject, default='คณิตศาสตร์')
    student_name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

    def __str__(self) -> str:
        return '{}-{}-{}'.format(self.subject, self.student_name, self.score)

class AllStudent(models.Model):
    levellist =(('ม.1', 'ม.1'),
                ('ม.2', 'ม.2'),
                ('ม.3', 'ม.3'),
                ('ม.4', 'ม.4'),
                ('ม.5', 'ม.5'),
                ('ม.6', 'ม.6'))
    
    level = models.CharField(max_length=100, choices=levellist, default='ม.1')
    student_name = models.CharField(max_length=200)
    student_id = models.CharField(max_length=200)
    student_tel = models.CharField(max_length=200, blank=True, null=True)
    parent_name = models.CharField(max_length=200, blank=True, null=True)
    parent_tel = models.CharField(max_length=200, blank=True, null=True)
    other = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="studentPhoto", blank=True, null=True)

    def __str__(self) -> str:
        return '{}-{}-{}'.format(self.student_id, self.student_name, self.level)
