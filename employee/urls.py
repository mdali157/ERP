from . import views
from django.conf.urls import url
from django.urls import path

app_name = 'employee'

urlpatterns = [
    path('employee/', views.employee_view, name='employeeview'),
    path('employees/<id>/', views.delete_employee, name='deleteemployee'),
    path('newemp/', views.newemp, name='newemp'),
    url(r'^(?P<id>[\w-]+)/$', views.employee_detail, name='employeedetail'),
    path('addEmployeepic/<id>', views.addpic, name='employeepic'),
    path('updateinformation/<id>/', views.update_employee_info, name='updateinfo'),

    path('salarysheet', views.salarysheet, name='salarysheet'),
    path('salarysheet/generatesalaryslip/', views.generatesalaryslip, name='generatesalaryslip'),
    path('salaryprint',views.salaryprint,name='salaryprint'),
    path('salaryprint1',views.salaryprint1,name='salaryprint1'),

    path('employee/monthlySheet/', views.monthlySheet,name='monthlySheet'),
    path('monthlysheetdetails/<id>/',views.monthlysheetdetails,name='monthlysheetdetails'),
    path('deletemonthlysheet/<id>/', views.deletemonthlysheet, name='deletemonthlysheet'),

    path('printmontlysalarysheet/<id>', views.printmothlysalarysheet, name='printmothlysalarysheet'),

]
