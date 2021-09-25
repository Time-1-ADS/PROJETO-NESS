from django.shortcuts import render
from core.models import Permission, Agent


def index(request):
    return render(request, 'main_screen.html')


def regcustumer(request):
    return render(request, 'customer_registration.html')
