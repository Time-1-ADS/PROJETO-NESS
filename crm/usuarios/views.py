from .forms import *
from django.shortcuts import render, redirect

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
            agente = form.save()
            form = CadastrarUsuario()
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, 'employee_registration.html', context=context)


    
