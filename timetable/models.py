from django.db import models
from staff.models import *

# Create your models here.

DAY_CHOICES = [
    ('mon', 'Monday'),
    ('tue', 'Tuesday'),
    ('wed', 'Wednesday'),
    ('thu', 'Thursday'),
    ('fri', 'Friday'),
]

class CreatTable(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)   
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)   
    table_class=models.ForeignKey(StudentClass,on_delete=models.CASCADE)
    #Class = models.CharField(max_length=250)
    stream=models.ForeignKey(ClassSection,on_delete=models.CASCADE,blank=True,null=True,default='Custom',help_text="Select custom if class has no sections")
    #stream=models.CharField(max_length=250)
    Stime = models.TimeField(help_text="Starting time")
    Etime = models.TimeField(help_text="Ending time")
    Day = models.CharField(max_length=3, choices=DAY_CHOICES)   

    def __str__(self):
        return self.subject
    
    class Meta:
        unique_together = ('subject', 'Stime', 'Etime')
        verbose_name_plural='Manage Timetable'
