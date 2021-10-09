from django.shortcuts import render, redirect
from core.models import Permission, Agent, Medic, Pipeline, Clinic, Empresa
from . import models
from .forms import AgentForm, MedicForm, PipeForm


def index(request):
    if request.method == "GET":
        context = {
            'form_pip': Pipeline.objects.all()
        }
        return render(request, 'main_screen.html', context=context)


def regcustumer(request):
    return render(request, 'customer_registration.html')


def contacts(request):
    tudo = Empresa.objects.all()
    context = {
        'contacts': tudo
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


def proposta(request):
    if request.method == "GET":
        form = PipeForm()
        context = {
            'form': form
        }
        return render(request, 'proposta.html', context=context)
    else:
        form = PipeForm(request.POST)
        if form.is_valid():
            agente = form.save()
            form = PipeForm()
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, 'proposta.html', context=context)


def atualizaProposta(request, pk):
    propos = Pipeline.objects.get(id=pk)
    form = PipeForm(instance=propos)
    if request.method == 'POST':
        form = PipeForm(request.POST, instance=propos)
        if form.is_valid():
            agente = form.save()
            form = PipeForm()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'proposta.html', context=context)


def deletaProposta(request, pk):
    propos = Pipeline.objects.get(id=pk)
    if request.method == 'POST':
        propos.delete()
        return redirect('index')
    context = {
        'prop': propos
    }
    return render(request, 'delete.html', context=context)
