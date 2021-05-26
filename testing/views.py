from django.http import HttpResponse, request
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from dashboard.models import ProjectModel
from dashboard.views import getProbations
from testing import forms
from testing.forms import addBugForm
from testing.models import Bugs


def Testprojects(request):
    projects = ProjectModel.objects.all()
    return render(request, 'testing/Testprojects.html', {'projects': projects})


#
def addBug(request):
    if request.method == 'POST':
        form = forms.addBugForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('testing:Testprojects')
    else:
        form: addBugForm = forms.addBugForm()
    return render(request, 'testing/add_bug.html', {'form': form})


def deletebug(request, id):
    obj = get_object_or_404(Bugs, id=id)
    obj.delete()

    return Testprojects(request)

def update_bugs(request, id):
    obj = Bugs.objects.get(id=id)
    form = addBugForm( instance=obj)
    if request.method == 'POST':
        form = addBugForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.save()
            return Testprojects(request)

    #     form = forms.addProjectForm()
    return render(request, 'testing/update_bug.html', {'form': form})

def delete_bug(request, id):
    obj = get_object_or_404(Bugs, id=id)
    obj.delete()
    id = request.POST.get('pid')
    return Testprojects(request)


def Projects_bugs(request, id):
    detail = ProjectModel.objects.get(id=id)
    return render(request, 'testing/bug_detail.html', {'id': id, 'detail': detail})


def addbug(request, id):
    prob = getProbations()
    count = prob.count()
    if request.method == 'POST':
        form = forms.addBugForm(request.POST, request.FILES)
        if form.is_valid():
            obj = ProjectModel.objects.get(id=id)
            print(obj)
            print("hi")
            r = form.save()
            obj.bugs.add(r)
            obj.save()
            return Projects_bugs(request, id)
            # return render(request, 'dashboard/dashboard_view.html')
    else:
        form = forms.addBugForm()
    return render(request, 'testing/add_bug.html', {'form': form, 'id': id, 'prob': prob, 'count': count})
