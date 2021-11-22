from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from core.models import Permission, Agent, Medic, Pipeline, Clinic, Empresa
from . import models
from .forms import AgentForm, DocumentForm, MedicForm, PipeForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required
def index(request):
    if request.method == "GET":
        context = {
            'form_pip': Pipeline.objects.all()
        }
        return render(request, 'main_screen.html', context=context)

@login_required
def regcustumer(request):
    return render(request, 'customer_registration.html')

@login_required
def contacts(request):
    medico = Medic.objects.all()
    context = {
        'contacts': medico,
    }
    return render(request, "contacts.html", context)

@login_required
def dashboard(request):
    leads = Pipeline.objects.all()

    opportunities = leads.filter(status='Novo')
    open = leads.filter(status='Aberto')
    pendente = leads.filter(status='Pendente')
    closed = leads.filter(status='Fechado')
    nmonitor = leads.filter(produto='nMonitor')
    nsensor = leads.filter(produto='nSensor')
    ncommand = leads.filter(produto='nCommand')
    necho = leads.filter(produto='nEcho')
    nreport = leads.filter(produto='nReport')
    iara = leads.filter(produto='Iara')
    


    leads_count = leads.count()
    opportunities_count = opportunities.count()
    open_count = open.count()
    pendent_count = pendente.count()
    closed_count = closed.count()
    nmonitor_count = nmonitor.count()
    nsensor_count = nsensor.count()
    ncommand_count = ncommand.count()
    necho_count = necho.count()
    nreport_count = nreport.count()
    iara_count = iara.count()

    

    if request.method=="GET":
        context = {
            'leads': leads_count,
            'oport': opportunities_count,
            'open': open_count,
            'pendent': pendent_count,
            'closed': closed_count,
            'nmonitor': nmonitor_count,
            'nsensor': nsensor_count,
            'ncommand': ncommand_count,
            'necho': necho_count,
            'nreport': nreport_count,
            'iara': iara_count
        }
    return render(request, 'dashboard.html', context=context)

@login_required
def register(request):
    return render(request, 'register.html')

@login_required
def leads(request):
    leads = Pipeline.objects.all()
    
    if request.method=="GET":
        context = {
            'titulo': leads
        }
    return render(request, 'leads.html', context=context)


@login_required
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

@login_required
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

@login_required
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

@login_required
def deletaProposta(request, pk):
    propos = Pipeline.objects.get(id=pk)
    if request.method == 'POST':
        propos.delete()
        return redirect('index')
    context = {
        'prop': propos
    }
    return render(request, 'delete.html', context=context)


def importacao(request):
    if request.method == "GET":
        form = DocumentForm()
        context = {
            'form': form
        }
        return render(request, 'importação.html', context=context)
    else:
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core.views.contacts'))
        context = {
            'form': form
        }