from django import forms
from . import models


class addBugForm(forms.ModelForm):
    class Meta:
        model = models.Bugs
        fields = { 'bug_title', 'bug_description','bug_pic'}

    def __init__(self, *args, **kwargs):
        super(addBugForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['style'] = 'height: 40px; width: 90%;'
            visible.field.widget.attrs['max'] = '1'
            visible.field.widget.attrs['min'] = '0'
            visible.field.widget.attrs[''] = 'required'

