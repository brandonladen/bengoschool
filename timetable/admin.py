from django.contrib import admin
from .models import CreatTable

# Register your models here.
class CreatTableAdmin(admin.ModelAdmin):
    list_display = ['staff','subject', 'table_class',"stream",'Stime', 'Etime', 'Day']

    def get_stream_names(self, obj):
        return ", ".join([stream.name for stream in obj.stream.all()])

admin.site.register(CreatTable,CreatTableAdmin)
