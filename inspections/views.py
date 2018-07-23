from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Inspection
from django.utils import timezone

def home(request):
    inpsections = Inspection.objects
    return render(request, 'inspections/home.html',{'inspections':inpsections})

@login_required(login_url="/accounts/signup")
def create(request):
    pass

def detail(request):
    return render(request, 'inspections/detail.html')

def home(request):
    return render(request, 'inspections/home.html')