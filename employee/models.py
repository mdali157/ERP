from django.db import models
from django.db.models import CASCADE


class Employeepic(models.Model):
    picture = models.ImageField(blank=True)


class EmployeeEducation(models.Model):
    institute = models.TextField(max_length=50)
    board = models.TextField(max_length=50)
    degree = models.TextField(max_length=50)
    startingdate = models.TextField(max_length=20)
    endingdate = models.TextField(max_length=20)
    result = models.TextField(max_length=10)
    percentage = models.IntegerField(default=None)

    def __str__(self):
        return self.institute


class EmployeeSkills(models.Model):
    skills = models.TextField(max_length=20)

    def __str__(self):
        return self.skills


class EmployeeExperience(models.Model):
    organization = models.TextField(max_length=20)
    previousDesignation = models.TextField(max_length=20)
    startingDate = models.TextField(max_length=20)
    endingDate = models.TextField(max_length=20)
    responsibilities = models.TextField(max_length=100)

    # abc = models.

    def __str__(self):
        return self.organization


# Create your models here.
class Employee(models.Model):
    boolChoice = (
        ("Male", "Male"), ("Female", "Female"))

    name = models.CharField(max_length=50)
    fname = models.TextField(max_length=50)
    CNIC = models.IntegerField(max_length=11)
    age = models.IntegerField(max_length=5)
    joiningdate = models.DateTimeField(max_length=20, blank=True, default=None)
    gender = models.CharField(max_length=10, choices=boolChoice)
    profile_pic = models.ImageField(default='place.png')
    salary = models.IntegerField(default=None)
    education = models.ManyToManyField(EmployeeEducation, default=None)
    experience = models.ManyToManyField(EmployeeExperience, default=None)
    skills = models.ManyToManyField(EmployeeSkills, default=None)

    def __str__(self):
        return self.name


class SalarySheet(models.Model):
    month = models.TextField(max_length=20, blank=True, default=None)

    def __str__(self):
        return self.month


class EmployeeSalaryCalculations(models.Model):
    emp = models.ForeignKey(Employee, on_delete=CASCADE, default=None)
    leaves = models.TextField(max_length=50, blank=True, default=None)
    leaveDeduction = models.IntegerField(max_length=51, )
    addition = models.IntegerField(max_length=50, default=0)
    deducation = models.IntegerField(max_length=50, default=0)
    total = models.IntegerField(max_length=50)
    salarysheet = models.ForeignKey(SalarySheet, on_delete=CASCADE)

    def __str__(self):
        return self.emp.name
