from django.shortcuts import render
#from .models import Engineering

def home(request):
    return render(request, 'services/home.html')

def engineering(request):
    return render(request, 'services/engineering.html')

def equipmentinspection(request):
    return render(request, 'services/equipmentinspection.html')

def fabrication(request):
    return render(request, 'services/fabrication.html')

def testing(request):
    return render(request, 'services/testing.html')

def toolinspection(request):
    return render(request, 'services/toolinspection.html')
