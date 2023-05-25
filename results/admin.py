from django.contrib import admin
from .models import *
# Register your models here.
class ResultAdmin(admin.ModelAdmin):
    list_display=['student','subject','test_score','exam_score','points_earned']

admin.site.register(Result,ResultAdmin)