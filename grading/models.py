from django.db import models
from authman.models import *
# Create your models here.
class Grades(models.Model):
    name=models.CharField(max_length=2,default=None)
    points=models.IntegerField(default=1)
    comment=models.TextField(max_length=255,default='Pass')

    class Meta:
        ordering=['name','comment']
        verbose_name_plural='Grades'
        managed=True

    def __str__(self):
        return self.name


class GradingLevel(models.Model):
    name=models.CharField(max_length=100,choices=(("highschool","Highschool"),("college","College"),("university","University")))
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='levels',blank=True,null=True)
    current=models.BooleanField(default=True,blank=True,null=True)

    class Meta:
        ordering=['name','course']
        verbose_name_plural='Grading Levels'
        managed=True
    def get_absolute_url(self):
        return reverse("grading-detail", kwargs={"pk": self.pk})



class GradingRules(models.Model):
    mark_range=models.CharField(max_length=10,default='0-0')
    grade=models.ForeignKey(Grades,on_delete=models.SET_NULL,default='A',null=True)
    grading_level = models.ForeignKey(
        GradingLevel,
        on_delete=models.CASCADE,
        related_name='grading_rules'
    )

    class Meta:
        ordering=['mark_range','grade']
        verbose_name_plural='Grading Rules'
        managed=True

    def get_absolute_url(self):
        return reverse("grading-detail", kwargs={"pk": self.pk})

class OverallGrading(models.Model):
    name=models.CharField(max_length=100,choices=(("highschool","Highschool"),("college","College"),("university","University")),default='highschool')
    current=models.BooleanField(default=True,blank=True,null=True)

    class Meta:
        ordering=['name',]
        verbose_name_plural='Overall Grading'
        managed=True

    # def __str__(self):
    #     return self.name
    def get_absolute_url(self):
        return reverse("overallgrading-detail", kwargs={"pk": self.pk})

class OveralGradingItem(models.Model):
    mark_range=models.CharField(max_length=10,default='0-0')
    points_range=models.CharField(max_length=10,default='0-0')
    grade=models.ForeignKey(Grades,on_delete=models.SET_NULL,default='A',null=True)
    overall_grading = models.ForeignKey(
        OverallGrading,
        on_delete=models.CASCADE,
        related_name='gradingitems'
    )

    class Meta:
        ordering=['mark_range','points_range','grade']
        verbose_name_plural='Overall Grading Rules'
        managed=True

    # def __str__(self):
    #     return f'{self.mark_range} - {self.grade}'
