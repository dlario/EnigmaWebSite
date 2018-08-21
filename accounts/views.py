from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import FormView
from inspections.models import Inspection
from accounts.models import Person, CompanyPerson, Company, ContactInformation
from accounts.forms import PersonForm

class personview(FormView):
    template_name = 'accounts/userdetails.html'
    form_class = PersonForm


def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])

                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'],
                                                password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')


def clientdetails(request):
    return render(request, 'accounts/clientdetails.html')


def clienthome(request):

    PersonAccount = Person.objects.filter(user=request.user).first()
    CompanyAccountPerson = CompanyPerson.objects.filter(person=PersonAccount).first()
    CompanyAccount = Company.objects.filter(id=CompanyAccountPerson.company.id).first()
    CompanyInspection = Inspection.objects.all()#filter(company=CompanyAccount)

    return render(request, 'accounts/clienthome.html', {'inspections': CompanyInspection, 'company': CompanyAccount, 'person': PersonAccount})


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        print(request.POST['username'], request.POST['password'])
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('clienthome')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('navhome')
