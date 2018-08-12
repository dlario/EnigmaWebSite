from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Inspection
from django.utils import timezone
from django.views.generic import FormView
from inspections.forms import SimpleForm, CreditCardForm, CartForm, Address
#def home(request):
#    inspection = Inspection.objects
#    return render(request, 'inspections/home.html',{'inspections':inspection})

class MainView(FormView):
    template_name = 'equipment/index.html'
    form_class = Address
    #return render(request, 'index.html', {'form': MessageForm()})
def home(request):
    return render (request, 'equipment/home.html')

#@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url']:
            inspection = Inspection()
            inspection.title = request.POST['title']
            inspection.insp_date = timezone.datetime.now()
            inspection.inspector = request.inspector
            inspection.save()
            return redirect('/inspections/' + str(inspection.id))
        else:
            return render(request, 'equipment/create.html')
    else:
        return render(request, 'equipment/create.html')