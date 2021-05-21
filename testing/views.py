from django.http import HttpResponse, request
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from testing import forms
from testing.forms import addBugForm
from testing.models import Bugs


def testingview(request):
    bug_report = Bugs.objects.all()
    return render(request, 'testing/testingview.html', {'bug_report': bug_report})


def addBug(request):
    if request.method == 'POST':
        form = forms.addBugForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('testing:testingview')
    else:
        form: addBugForm = forms.addBugForm()
    return render(request, 'testing/add_bug.html', {'form': form})

def deletebug(request, id):
    obj = get_object_or_404(Bugs, id=id)
    obj.delete()

    return testingview(request)

def updatebug(request, id):
    acc = Bugs.objects.get(id=id)
    form = addBugForm(instance=acc)
    print(id)
    if request.method == 'POST':
        form = addBugForm(request.POST, instance=acc)
        if form.is_valid():
            form.save()
            return redirect('testing:testingview')

    context = {'form': form}
    return render(request, 'testing/update_bug.html', context)

def bug_detail(request, id):
    bug_report = Bugs.objects.get(id=id)
    return render(request, 'testing/bug_detail.html',{ 'id': id,'bug_report':bug_report })


