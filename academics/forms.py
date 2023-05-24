from django import forms
from django.forms.widgets import DateInput, TextInput
from django.forms import widgets
from django.forms import ModelForm, modelformset_factory

from .models import *

SiteConfigForm = modelformset_factory(
    SiteConfig,
    fields=(
        "key",
        "value",
    ),
    extra=0,
)


class AcademicSessionForm(ModelForm):
    prefix = "Academic Session"
    def __init__(self, *args, **kwargs):
        super(AcademicSessionForm, self).__init__(*args, **kwargs)
        self.fields["from_date"].widget = widgets.DateInput(attrs={"type": "date","class":"form-control"})
        self.fields["to_date"].widget = widgets.DateInput(attrs={"type": "date","class":"form-control"})


    class Meta:
        model = AcademicSession
        fields = ["name","from_date","to_date","current"]


class AcademicTermForm(ModelForm):
    prefix = "Academic Term"

    class Meta:
        model = AcademicTerm
        fields = ["name", "current"]


class StudentClassForm(ModelForm):
    prefix = "Class"

    class Meta:
        model = StudentClass
        fields = ["name"]


class CurrentSessionForm(forms.Form):
    current_session = forms.ModelChoiceField(
        queryset=AcademicSession.objects.all(),
        help_text='Click <a href="/session/create/?next=current-session/">here</a> to add new session',
    )
    current_term = forms.ModelChoiceField(
        queryset=AcademicTerm.objects.all(),
        help_text='Click <a href="/term/create/?next=current-session/">here</a> to add new term',
    )
