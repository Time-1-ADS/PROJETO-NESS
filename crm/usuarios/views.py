from django.contrib.auth import authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.http.response import HttpResponseRedirect

from core.forms import AgentForm
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_protect
from core.models import Agent
from django.contrib.auth.decorators import login_required


@login_required
def usercadastrado(request):
    if request.method == "GET":
        form = CadastrarUsuario()
        context = {
            'form': form
        }
        return render(request, 'employee_registration.html', context=context)
    else:
        form = CadastrarUsuario(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            pwd = make_password(form.cleaned_data['password'])
            cargo_id = form.data['cargo']

            user = Agent(first_name=first_name, last_name=last_name,
                         username=username, email=email, password=pwd, cargo_id=cargo_id)
            user.save()
            return redirect('Login')
        context = {
            'form': form
        }
        return render(request, 'employee_registration.html', context=context)


def login(request):
    return render(request, 'login.html')


@csrf_protect
def logar(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return redirect('Login')


@login_required
def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/')

# @login_required
# def profile(request, pk):
#     model = Agent.objects.get(id=pk)
#     form = AgentForm(instance=model)
#     context = {
#         'prof': form
#     }
#     return render(request, 'profile.html', context=context)
