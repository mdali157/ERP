from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models


class addProjectForm(forms.ModelForm):
    class Meta:
        model = models.ProjectModel
        fields = {'title', 'projectDescription', 'status'}

    def __init__(self, *args, **kwargs):
        super(addProjectForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class addProjectRequirment(forms.ModelForm):
    class Meta:
        model = models.Requirement
        fields = {'title', 'description', 'status'}

    def __init__(self, *args, **kwargs):
        super(addProjectRequirment, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

