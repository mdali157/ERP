
from django.shortcuts import render, redirect
from django.http import HttpResponse


def homepage(request):
    return render(request, 'login_page.html')


def client(request):
    return render(request,'client.html')
    # return HttpResponse("asdsa")