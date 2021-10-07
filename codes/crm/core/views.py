from django.shortcuts import render, redirect
from core.models import Permission, Agent, Medic, Pipeline
from . import models
from .forms import AgentForm, MedicForm, PipeForm


def index(request):
    if request.method == "GET" or "POST":
        if request.method == "GET":
            form_pip = PipeForm()
            context = {
                'form_pip': form_pip
            }
            return render(request, 'main_screen.html', context=context)
        else:
            form_pip = PipeForm(request.POST)
            if form_pip.is_valid():
                pipe = form_pip.save()
                form = PipeForm()
                return redirect('index')
            context = {
                'form_pip': form_pip
            }
            return render(request, 'main_screen.html', context=context)
    else:
        context = {
            'pipelines': Pipeline.objects.all()
        }
        return render(request, 'main_screen.html', context=context)


def regcustumer(request):
    return render(request, 'customer_registration.html')


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


def form_agent(request):
    if request.method == "GET":
        form = AgentForm()
        context = {
            'form': form
        }
        return render(request, 'employee_registration.html', context=context)
    else:
        form = AgentForm(request.POST)
        if form.is_valid():
            agente = form.save()
            form = AgentForm()
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, 'employee_registration.html', context=context)


def form_medic(request):
    if request.method == "GET":
        form = MedicForm()
        context = {
            'form': form
        }
        return render(request, 'customer_registration.html', context=context)
    else:
        form = MedicForm(request.POST)
        if form.is_valid():
            agente = form.save()
            form = MedicForm()
            return redirect('Contacts')
        context = {
            'form': form
        }
        return render(request, 'customer_registration.html', context=context)
