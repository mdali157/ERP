from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from FYP_ERM.decorators import unauthenticated_user
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForms
from django.contrib import messages
from django.contrib.auth.models import Group




# Create your views here.
def logout_views(request):
    if request.method == 'POST':
        logout(request)
        return redirect('dashboard:dashboard_view')

@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('dashboard:dashboard_view')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@unauthenticated_user
def register_view(request):
    form = CreateUserForms()

    if request.method == 'POST':
        form = CreateUserForms(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='client')
            user.groups.add(group)

            messages.success(request, 'Account was Successfully created for ' + username)
            return redirect('accounts:login')

    context = {'form':form}
    return render(request,'accounts/register.html',context)