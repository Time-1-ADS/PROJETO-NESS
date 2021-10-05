from django.shortcuts import render
from core.models import Permission, Agent, Medic
from . import models
from .forms import *
from django.views.generic.list import ListView
from django.contrib.auth.hashers import make_password


def index(request):
    return render(request, 'main_screen.html')


def regcustumer(request):
    return render(request, 'customer_registration.html')


def regemployee(request):
    form = AgentForm(request.POST or None)
    if form.is_valid():
        agent = form.save(commit=False)
        agent.senha = make_password(request.POST['senha'])
        agent.save()
        # return redirect('Employee')
    return render(request, 'employee_registration.html', {'form': form})


def contacts(request):
    context = {
        'contacts': Medic.objects.all()
    }
    return render(request, "contacts.html", context)


def dashboard(request):
    return render(request, 'dashboard.html')


def register(request):
    return render(request, 'register.html')


def leads(request):
    return render(request, 'leads.html')


def employee(request):
    context = {
        'funcs': Agent.objects.all()
    }
    return render(request, 'employee.html', context)
