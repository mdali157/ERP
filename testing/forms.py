from django import forms
from . import models


class addBugForm(forms.ModelForm):
    class Meta:
        model = models.Bugs
        fields = {'project_title', 'bug_title', 'bug_description',}

    def __init__(self, *args, **kwargs):
        super(addBugForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
