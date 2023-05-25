from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from authman.models import *
from academics.models import *
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = CustomUser(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    USER_TYPE = ((1, "HOD"), (2, "Staff"), (3, "Student"))
    GENDER = [("M", "Male"), ("F", "Female"), ("O", "Other")]
    username = models.CharField(max_length=150, unique=True,blank=True,null=True)
    email = models.EmailField(unique=True)
    user_type = models.CharField(default=1, choices=USER_TYPE, max_length=1)
    gender = models.CharField(max_length=1, choices=GENDER)
    profile_pic = models.ImageField()
    other_name = models.CharField(max_length=200, blank=True)
    address = models.TextField()
    fcm_token = models.TextField(default="")  # For firebase notifications
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = slugify(self.email.split('@')[0])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.last_name + ", " + self.first_name


class Admin(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Staff(models.Model):
    STATUS = [("active", "Active"), ("inactive", "Inactive")]
    current_status = models.CharField(
        max_length=10, choices=STATUS, default="active")
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    course = models.ManyToManyField("Course",blank=True, null=True)
    date_of_birth = models.DateField(default=timezone.now)
    date_of_admission = models.DateField(default=timezone.now)
    mobile_num_regex = RegexValidator(
        regex=r"^(?:\+254|0)[17]\d{8}$", message="Entered mobile number isn't in a right format!"
    )
    mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=13, blank=True
    )
    address = models.TextField(blank=True)
    others = models.TextField(blank=True)

    def __str__(self):
        return self.admin.email

    def get_absolute_url(self):
        return reverse("staff-detail", kwargs={"pk": self.pk})

class Parent(models.Model):
    STATUS = [("active", "Active"), ("inactive", "Inactive")]
    current_status = models.CharField(
        max_length=10, choices=STATUS, default="active")
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    date_of_birth = models.DateField(default=timezone.now)
    mobile_num_regex = RegexValidator(
        regex=r"^(?:\+254|0)[17]\d{8}$", message="Entered mobile number isn't in a right format!"
    )
    mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=13, blank=True
    )
    address = models.TextField(blank=True)

    def __str__(self):
        return self.admin.email

    def get_absolute_url(self):
        return reverse("staff-detail", kwargs={"pk": self.pk})


class Course(models.Model):
    name = models.CharField(max_length=255, default='Highschool Education')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Subject(models.Model):
    name = models.CharField(max_length=120)
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE,)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    STATUS_CHOICES = [("active", "Active"), ("inactive", "Inactive")]
    current_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active"
    )
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=200, unique=True)
    date_of_birth = models.DateField(default=timezone.now)
    current_class = models.ForeignKey(
        StudentClass, on_delete=models.SET_NULL, blank=True, null=True
    )
    course = models.ForeignKey(
        Course, on_delete=models.SET_NULL, default=1, blank=True, null=True)
    session = models.ForeignKey(
        AcademicSession, on_delete=models.SET_NULL, null=True)
    date_of_admission = models.DateField(default=timezone.now)
    parent = models.ForeignKey(Parent,on_delete=models.CASCADE,related_name='students',blank=True,null=True)
    others = models.TextField(blank=True)
    passport = models.ImageField(blank=True, upload_to="students/passports/")

    class Meta:
        ordering = ["id", "current_class"]

    def __str__(self):
        return self.registration_number


    def get_absolute_url(self):
        return reverse("student-detail", kwargs={"pk": self.pk})


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):  
    if created:
        if instance.user_type == 1:
            Admin.objects.create(admin=instance)
        if instance.user_type == 2:
            Staff.objects.create(admin=instance)
        if instance.user_type == 3:
            Student.objects.create(admin=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin.save()
    if instance.user_type == 2:
        instance.staff.save()
    if instance.user_type == 3:
        instance.student.save() 