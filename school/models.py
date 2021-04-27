from django.db import models
from django.db.models.base import Model

# Create your models here.
class ExamScore(models.Model):
    allSubject = (('คณิตศาสตร์', 'คณิตศาสตร์'),
                    ('วิทยาศาสตร์', 'วิทยาศาสตร์'),
                    ('ศิลปะ', 'ศิลปะ'),
                    ('ภาษาอังกฤษ', 'ภาษาอังกฤษ'),
                    ('ฟิสิกส์', 'ฟิสิกส์'),
                    ('ชีววิทยา', 'ชีววิทยา'))

    subject = models.CharField(max_length=200, choices=allSubject, default='math')
    student_name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.student_name + '-' + self.subject + '-' + str(self.score)


