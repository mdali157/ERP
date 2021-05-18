from django.shortcuts import render

# Create your views here.
from employee.models import Employee


def attendanceview(request):
    employee = Employee.objects.all()
    return  render(request, 'attendance/attendance_view.html',{'employee':employee})