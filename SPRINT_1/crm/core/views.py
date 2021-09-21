from django.shortcuts import render


def index(request):
    return render(request, '../static/templates/main_screen.html')
