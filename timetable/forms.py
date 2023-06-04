from django import forms
from .models import CreatTable
from django.forms.widgets import *


class tableForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(tableForm, self).__init__(*args, **kwargs)
        # Here make some changes such as:
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = CreatTable
        fields = "__all__"
        widgets = {
            'Stime': TimeInput(attrs={'type': 'time'}),
            'Etime': TimeInput(attrs={'type': 'time'}),
        }
