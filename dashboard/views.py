from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import forms
from .forms import addProjectForm, addProjectRequirment
from employee.models import Employee
from .models import ProjectModel, Requirement
from FYP_ERM.decorators import allowed_users,admin_only
import datetime


@login_required(login_url='/accounts/login')
@admin_only
def dashboard_view(request):

    prob = getProbations()
    print(prob)
    count = prob.count()
    print(count)
    return render(request, 'dashboard/dashboard_view.html',{'prob':prob,'count':count})

def getProbations():
    now = datetime.datetime.now()
    past = now - datetime.timedelta(days=90)
    employees = Employee.objects.filter(joiningdate__lte=past)
    return employees

@allowed_users(allowed_role=['admin'])
@login_required(login_url='/accounts/login')
def project_view(request):
    projects = ProjectModel.objects.all()
    prob = getProbations()
    count = prob.count()

    return render(request, 'dashboard/project_view.html', {'projects': projects,'prob':prob,'count':count})

@login_required(login_url='/accounts/login')
@allowed_users(allowed_role=['admin'])
def addProject(request):
    prob = getProbations()
    count = prob.count()
    if request.method == 'POST':
        form = forms.addProjectForm(data=request.POST)
        if form.is_valid():
            form.save()
            return project_view(request)
            # return render(request, 'dashboard/dashboard_view.html')
    else:
        form = forms.addProjectForm()
    return render(request, 'dashboard/add_project.html', {'form': form,'prob':prob,'count':count})
    # return render(request, 'dashboard/project_view.html')

@login_required(login_url='/accounts/login')
@allowed_users(allowed_role=['admin'])
def delete_project(request, id):
    obj = get_object_or_404(ProjectModel, id=id)
    obj.delete()
    return project_view(request)

@login_required(login_url='/accounts/login')
@allowed_users(allowed_role=['admin'])
def delete_requirment(request, id):
    obj = get_object_or_404(Requirement, id=id)
    obj.delete()
    id = request.POST.get('pid')
    return project_detail(request, id)


@login_required(login_url='/accounts/login')
@allowed_users(allowed_role=['admin'])
def update_project(request, id):
    prob = getProbations()
    count = prob.count()
    obj = ProjectModel.objects.get(id=id)
    form = addProjectForm(data=request.POST or None, instance=obj)
    if request.method == 'POST':
        # form = addProjectForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return project_view(request)

    #     form = forms.addProjectForm()
    return render(request, 'dashboard/add_project.html', {'form': form,'prob':prob,'count':count})

@allowed_users(allowed_role=['admin'])
@login_required(login_url='/accounts/login')
def project_detail(request, id):
    detail = ProjectModel.objects.get(id=id)
    prob = getProbations()
    count = prob.count()

    return render(request, 'dashboard/project_details.html', {'detail': detail, 'id': id,'prob':prob,'count':count})

@allowed_users(allowed_role=['admin'])
@login_required(login_url='/accounts/login')
def add_requrement(request, id):
    prob = getProbations()
    count = prob.count()
    if request.method == 'POST':
        form = forms.addProjectRequirment(data=request.POST)
        if form.is_valid():
            obj = ProjectModel.objects.get(id=id)
            print(obj)
            print("hi")
            r = form.save()
            obj.requirement.add(r)
            obj.save()
            return project_detail(request, id)
            # return render(request, 'dashboard/dashboard_view.html')
    else:
        form = forms.addProjectRequirment()
    return render(request, 'dashboard/add_requirment.html', {'form': form, 'id': id,'prob':prob,'count':count})


@login_required(login_url='/accounts/login')
@allowed_users(allowed_role=['admin'])
def update_requirements(request, id):
    obj = Requirement.objects.get(id=id)
    form = addProjectRequirment(data=request.POST or None, instance=obj)
    if request.method == 'POST':
        # form = addProjectForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/')

    #     form = forms.addProjectForm()
    return render(request, 'dashboard/add_requirment.html', {'form': form})

