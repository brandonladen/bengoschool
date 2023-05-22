from django.forms import ModelForm,inlineformset_factory,formset_factory
from django import forms
from .models import *

GradingItemFormset = inlineformset_factory(
    GradingLevel, GradingRules, fields=["mark_range", "grade"], extra=1, can_delete=True
)

OverallGradingFormSet =inlineformset_factory(
    OverallGrading, OveralGradingItem, fields=["mark_range","points_range", "grade"], extra=1, can_delete=True
)

class GradesForm(ModelForm):
    prefix = "Grades"

    class Meta:
        model = Grades
        fields = '__all__'

class GradingLevelForm(ModelForm):
    prefix = "Grading Level"

    class Meta:
        model = GradingLevel
        fields = ["name","course","current"]


class CurrentLevelForm(forms.Form):
    current_level = forms.ModelChoiceField(
        queryset=GradingLevel.objects.all(),
        help_text='Click <a href="/grading/gradinglevel/create/?next=current-level/">here</a> to add new Level',
    )
