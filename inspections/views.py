from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Inspection
from django.utils import timezone

def home(request):
    inspection = Inspection.objects
    return render(request, 'inspections/home.html',{'inspections':inspection})

@login_required(login_url="/accounts/signup")
def create(request):
    pass

def home(request):
    return render(request, 'inspections/home.html')

def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url']:
            inspection = Inspection()
            inspection.title = request.POST['title']
            inspection.icon = request.FILES['icon']
            inspection.image = request.FILES['image']
            inspection.insp_date = timezone.datetime.now()
            inspection.inspector = request.inspector
            inspection.save()
            return redirect('/inspections/' + str(inspection.id))
        else:
            return render(request, 'inspection/create.html')
    else:
        return render(request, 'inspection/create.html')

def detail(request, inspection_id):
    inspection = get_object_or_404(Inspection, pk=inspection_id)
    return render(request, 'inspections/detail.html', {'inspection':inspection})