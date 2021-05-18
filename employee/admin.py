from django.contrib import admin

# Register your models here.
from employee.models import Employee, EmployeeEducation, EmployeeSkills, EmployeeExperience,Employeepic,SalarySheet,EmployeeSalaryCalculations


admin.site.register(Employee)
admin.site.register(EmployeeEducation)
admin.site.register(EmployeeSkills)
admin.site.register(EmployeeExperience)
admin.site.register(Employeepic)
admin.site.register(SalarySheet)
admin.site.register(EmployeeSalaryCalculations)
