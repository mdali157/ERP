from itertools import count

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import forms
from .forms import addEmployeeform
from .models import Employee, EmployeeEducation, EmployeeExperience, EmployeeSkills, Employeepic, SalarySheet, \
    EmployeeSalaryCalculations
from FYP_ERM.decorators import allowed_users
from datetime import datetime
from calendar import monthrange
from dashboard.views import getProbations


@login_required(login_url='/accounts/login')
@allowed_users(allowed_role=['admin'])
def employee_view(request):
    employee = Employee.objects.all()
    prob = getProbations()
    count = prob.count()
    return render(request, 'employee/employee_view.html', {'employee': employee,"prob":prob,'count':count})


@login_required(login_url='/accounts/login')
@allowed_users(allowed_role=['admin'])
def delete_employee(request, id):
    obj = get_object_or_404(Employee, id=id)

    obj.experience.clear()
    obj.education.remove()
    obj.delete()

    return employee_view(request)


@login_required(login_url='/accounts/login')
@allowed_users(allowed_role=['admin'])
def employee_detail(request, id):
    detail = Employee.objects.get(id=id)
    prob = getProbations()
    count = prob.count()
    if request.method == 'POST':
        form = forms.addEmployeepic(request.POST, request.FILES)
        if form.is_valid():
            obj = Employee.objects.get(id=id)
            r = form.save()
            print("---------- 1st")
            obj.profile_pic = request.FILES['picture'].name
            print("----------")
            obj.save()
            return employee_detail(request, id)
    else:
        form = forms.addEmployeepic()
    return render(request, 'employee/employee_details.html', {'detail': detail, 'id': id, 'form': form,'count':count,'prob':prob})


def newemp(request):
    prob = getProbations()
    count = prob.count()
    if request.POST:
        firstname = request.POST.get("fname")
        fathername = request.POST.get("lname")
        id_cnic = request.POST.get("cnic")
        aging = request.POST.get("age")
        sex = request.POST.get("gender")
        pay = request.POST.get("salary")
        joiningdate = request.POST.get("joiningdate")

        # education

        inslist = request.POST.getlist("Institute[]")
        boardlist = request.POST.getlist("Board_Uni[]")
        degreelist = request.POST.getlist("Degree[]")
        startingdatelist = request.POST.getlist("PassingYear[]")
        endingdatelist = request.POST.getlist("enddate[]")
        resultlist = request.POST.getlist("Result[]")
        percentagelist = request.POST.getlist("Number_CGPA[]")

        # Experience

        orglist = request.POST.getlist("Organization[]")
        pdlist = request.POST.getlist("Previous_Designation[]")
        fromdlist = request.POST.getlist("FromDate[]")
        todlist = request.POST.getlist("ToDate[]")
        reslist = request.POST.getlist("Responsibility[]")

        # skiils
        chklist = request.POST.getlist('chkbox[]')

        obj = Employee(name=firstname, fname=fathername, CNIC=id_cnic, age=aging, gender=sex, salary=pay, joiningdate=joiningdate)
        obj.save()
        # object = Employee.objects.all()
        for i in range(len(inslist)):
            print(i)

            edu = EmployeeEducation(institute=inslist[i], board=boardlist[i], degree=degreelist[i],
                                    startingdate=startingdatelist[i], endingdate=endingdatelist[i],
                                    result=resultlist[i], percentage=percentagelist[i])
            edu.save()
            obj.education.add(edu)
            obj.save()

        for i in range(len(orglist)):
            exp = EmployeeExperience(organization=orglist[i], previousDesignation=pdlist[i], startingDate=fromdlist[i],
                                     endingDate=todlist[i], responsibilities=reslist[i])
            exp.save()
            obj.experience.add(exp)
            obj.save()

        for i in range(len(chklist)):
            skl = EmployeeSkills(skills=chklist[i])
            skl.save()
            obj.skills.add(skl)
            obj.save()
        return employee_view(request)
    return render(request, 'employee/add_employee.html',{'count':count,'prob':prob})


def addpic(request, id):
    if request.method == 'POST':
        form = forms.addEmployeepic(request.POST, request.FILES)
        if form.is_valid():
            obj = Employee.objects.get(id=id)
            r = form.save()
            print("---------- 1st")

            obj.profile_pic = request.FILES['picture'].name

            print("----------")
            obj.save()
            return employee_detail(request, id)
    else:
        form = forms.addEmployeepic()
    return render(request, 'employee/add_employee_pic.html', {'form': form, 'id': id})


def update_employee_info(request, id):
    prob = getProbations()
    count = prob.count()
    emp = Employee.objects.get(id=id)
    skill = EmployeeSkills.objects.filter(employee=emp)
    skillList = []
    for s in skill:
        print(s.skills)
        skillList.append(s.skills)

    if request.POST:
        firstname = request.POST.get("fname")
        fathername = request.POST.get("lname")
        id_cnic = request.POST.get("cnic")
        aging = request.POST.get("age")
        sex = request.POST.get("gender")
        pay = request.POST.get("salary")

        # education
        inslist = request.POST.getlist("Institute[]")
        boardlist = request.POST.getlist("Board_Uni[]")
        degreelist = request.POST.getlist("Degree[]")
        startingdatelist = request.POST.getlist("PassingYear[]")
        endingdatelist = request.POST.getlist("enddate[]")
        resultlist = request.POST.getlist("Result[]")
        percentagelist = request.POST.getlist("Number_CGPA[]")

        # Experience
        orglist = request.POST.getlist("Organization[]")
        pdlist = request.POST.getlist("Previous_Designation[]")
        fromdlist = request.POST.getlist("FromDate[]")
        todlist = request.POST.getlist("ToDate[]")
        reslist = request.POST.getlist("Responsibility[]")

        # skiils
        chklist = request.POST.getlist('chkbox[]')

        emp.name = firstname
        emp.fname = fathername
        emp.CNIC = id_cnic
        emp.age = aging
        emp.gender = sex
        emp.salary = pay
        emp.save()

        emp.education.clear()
        for i in range(len(inslist)):
            print(i)
            edu = EmployeeEducation(institute=inslist[i], board=boardlist[i], degree=degreelist[i],
                                    startingdate=startingdatelist[i], endingdate=endingdatelist[i],
                                    result=resultlist[i], percentage=percentagelist[i])
            edu.save()
            emp.education.add(edu)
            emp.save()
        print('----------------------------------------')

        emp.experience.clear()
        for i in range(len(orglist)):
            exp = EmployeeExperience(organization=orglist[i], previousDesignation=pdlist[i],
                                     startingDate=fromdlist[i],
                                     endingDate=todlist[i], responsibilities=reslist[i])
            exp.save()
            emp.experience.add(exp)
            emp.save()

        emp.skills.clear()

        for i in range(len(chklist)):
            skl = EmployeeSkills(skills=chklist[i])
            skl.save()
            emp.skills.add(skl)
            emp.save()
        return employee_view(request)

    return render(request, 'employee/update_emp.html', {'emp': emp, 'id': id, 'skillList': skillList,'count':count,'prob':prob})


def salarysheet(request):
    employee = Employee.objects.all()
    prob = getProbations()
    count = prob.count()
    return render(request, 'employee/salary_sheet_view.html', {'employee': employee,'count':count,'prob':prob})


def salaryprint(request):
    employee = Employee.objects.all()
    employeecal = EmployeeSalaryCalculations.objects.all()
    prob = getProbations()
    count = prob.count()
    return render(request, 'employee/Salary_Print_view.html', {'employee': employee, 'employeecal': employeecal,'prob':prob,'count':count})


def generatesalaryslip(request):
    employee = Employee.objects.all()
    employeeList = request.POST.getlist('employeeList[]')

    if request.POST:

        month = request.POST.get('month')
        time = datetime.strptime(month, '%Y-%m')
        m = time.strftime('%m')
        y = time.strftime('%y')
        daysofmonth = (monthrange(int(y), int(m))[1])
        print(daysofmonth)
        print("---------------------")

        sSheet = SalarySheet.objects.filter(month=month).first()
        if (sSheet):
            request.method = 'GET'
            return render(request, 'employee/Salary_Print_view.html', {'employee': employee, 'flag': 1})

        else:
            sSheet = SalarySheet()
            sSheet.month = month
            sSheet.save()

            for e in employeeList:
                eSheet = EmployeeSalaryCalculations()

                # print(e)
                l = request.POST.get(e)
                print(l)

                emp = Employee.objects.get(id=e)
                salary = emp.salary
                print(salary)
                perday = salary / daysofmonth
                print((perday))

                salaryded = perday * int(l)
                print(salaryded)

                addition = request.POST.get('a' + e)
                sub = request.POST.get('s' + e)

                print("----")

                ssub = salaryded + int(sub)
                print(ssub)
                addd = salary + int(addition)
                print(addd)
                netsalary = addd - ssub

                print("----")

                print("netsalary = ")
                print(int(netsalary))

                eSheet.emp = emp
                eSheet.leaves = l
                eSheet.addition = addition
                eSheet.deducation = sub
                eSheet.salarysheet = sSheet
                eSheet.total = netsalary
                eSheet.leaveDeduction = salaryded
                eSheet.save()

        return monthlysheetdetails(request, sSheet.id)
    return render(request, 'employee/Salary_Print_view.html', {'employee': employee})


def salaryprint1(request):
    employee = Employee.objects.all()
    employeecal = EmployeeSalaryCalculations.objects.all()

    return render(request, 'employee/salaryprint1.html', {'employee': employee, 'employeecal': employeecal})


def monthlySheet(request):
    sheet = SalarySheet.objects.all()
    prob = getProbations()
    count = prob.count()
    return render(request, 'employee/monthlySheet.html', {'sheet': sheet,'prob':prob,'count':count})


def monthlysheetdetails(request, id):
    m = SalarySheet.objects.get(id=id)
    viewsheet = EmployeeSalaryCalculations.objects.filter(salarysheet=m)
    prob = getProbations()
    count = prob.count()
    return render(request, 'employee/monthlysheetdetails.html', {'sheet': viewsheet, 'm': m,'count':count,'prob':prob})


def deletemonthlysheet(request, id):
    obj = get_object_or_404(SalarySheet, id=id)
    obj.delete()

    return monthlySheet(request)


def printmothlysalarysheet(request, id):
    m = SalarySheet.objects.get(id=id)
    viewsheet = EmployeeSalaryCalculations.objects.filter(salarysheet=m)
    return render(request, 'employee/printmontlysalarysheet.html', {'sheet': viewsheet, 'm': m})

