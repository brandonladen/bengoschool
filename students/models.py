from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from academics.models import *
from authman.models import *


class StudentBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="students/bulkupload/")
