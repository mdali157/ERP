from django.shortcuts import render

# Create your views here.
from employee.models import Employee
from dashboard.views import getProbations


def attendanceview(request):
    employee = Employee.objects.all()
    prob = getProbations()
    count = prob.count()
    return render(request, 'attendance/attendance_view.html', {'employee': employee, "prob":prob,'count':count})
