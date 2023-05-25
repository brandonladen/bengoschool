from django.db import models

from academics.models import *
from students.models import Student
from authman.models import *
from .utils import *
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
    term = models.ForeignKey(AcademicTerm, on_delete=models.CASCADE)
    current_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    current_section = models.ForeignKey(ClassSection, on_delete=models.CASCADE,default=None,null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    test_score = models.IntegerField(default=0)
    exam_score = models.IntegerField(default=0)
    points_earned=models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["subject"]

    def __str__(self):
        return f"{self.student} {self.session} {self.term} {self.subject}"

    def total_score(self):
        return self.test_score + self.exam_score

    def grade(self):
        return score_grade(self.total_score(),self.subject.course)
