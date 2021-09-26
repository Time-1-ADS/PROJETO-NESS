from django.shortcuts import render
from core.models import Permission, Agent, Medic
from . import models
from django.views.generic.list import ListView


def index(request):
    return render(request, 'main_screen.html')


def regcustumer(request):
    return render(request, 'customer_registration.html')


def regemployee(request):
    return render(request, 'employee_registration.html')


def contacts(request):
    context = {
        'contacts': Medic.objects.all()
    }
    return render(request, "contacts.html", context)


def dashboard(request):
    return render(request, 'dashboard.html')
