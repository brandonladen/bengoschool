from django.db import models

# Create your models here.


class SiteConfig(models.Model):
    """Site Configurations"""

    key = models.SlugField()
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.key

class SchoolSetup(models.Model):
    logo=models.ImageField(upload_to='school_logo/',default='school_logo/default.png')

    def __str__(self):
        return self.logo.url if self.logo else 'school_logo/default.png'

    class Meta:
        verbose_name_plural='School Setup'





class AcademicSession(models.Model):
    """Academic Session"""
    name = models.CharField(max_length=200, unique=True)
    from_date=models.DateField(null=True,blank=True)
    to_date=models.DateField(null=True,blank=True)
    current = models.BooleanField(default=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


class AcademicTerm(models.Model):
    """Academic Term"""

    name = models.CharField(max_length=20, unique=True)
    current = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class StudentClass(models.Model):
    name = models.CharField(max_length=200, unique=True)
    sections = models.ManyToManyField("ClassSection")

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
        ordering = ["name"]

    def __str__(self):
        return self.name


class ClassSection(models.Model):
    name = models.CharField(max_length=200,default="Custom")

    class Meta:
        verbose_name = "Class Section"
        verbose_name_plural = "Class Sections"
        ordering = ["name"]

    def __str__(self):
        return self.name
