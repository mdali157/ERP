from django import forms
from . import models


class addEmployeeform(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = {'name', 'CNIC', 'age','profile_pic', 'gender', 'education', 'skills', 'experience'}

    def __init__(self, *args, **kwargs):
        super(addEmployeeform, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class addEmployeepic(forms.ModelForm):
    class Meta:
        model = models.Employeepic
        fields = {'picture'}

    def __init__(self, *args, **kwargs):
        super(addEmployeepic, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
