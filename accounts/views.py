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
    if request.method == 'POST':
        '''print(request.POST.get('bcompanyname'))
        print(request.POST.get('bfirstname'))
        print(request.POST.get('blastname'))
        print(request.POST.get('busername'))
        print(request.POST.get('bemail'))
        print(request.POST.get('baddress'))
        print(request.POST.get('baddress2'))
        print(request.POST.get('bcountry'))
        print(request.POST.get('bprovince'))
        print(request.POST.get('bpostalcode'))'''

        #TODO: Create a database recording changes in tranactions. Have the server know which ones were updated
        PersonAccount = Person.objects.filter(user=request.user).first()
        PersonAccount.first_name = request.POST.get('firstname')
        PersonAccount.last_name = request.POST.get('lastname')
        PersonAccount.save()

        user = User.objects.get(username=request.POST['username'])
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.email = request.POST.get('email')
        user.save()

        CompanyAccountPerson = CompanyPerson.objects.filter(person=PersonAccount).first()
        CompanyAccount = Company.objects.filter(id=CompanyAccountPerson.company.id).first()

        CompanyAccount.company_name = request.POST.get('companyname')
        #CompanyAccount.city = request.POST.get('firstname')
        CompanyAccount.province = request.POST.get('province')
        CompanyAccount.address = request.POST.get('address')
        CompanyAccount.box_number = request.POST.get('firstname')
        CompanyAccount.postal_code = request.POST.get('postalcode')

        CompanyInspection = Inspection.objects.all()  # filter(company=CompanyAccount)

        return render(request, 'accounts/clienthome.html',
                      {'inspections': CompanyInspection, 'company': CompanyAccount, 'person': PersonAccount})
    else:
        UserDate = request.user
        PersonAccount = Person.objects.filter(user=request.user).first()
        CompanyAccountPerson = CompanyPerson.objects.filter(person=PersonAccount).first()
        CompanyAccount = Company.objects.filter(id=CompanyAccountPerson.company.id).first()
        return render(request, 'accounts/clientdetails.html', {'company': CompanyAccount, 'person': PersonAccount})

def savedetails(request):
    if request.method == 'POST':
        print(request.POST['companyname'])
        print(request.POST['firstName'])
        print(request.POST['lastName'])
        print(request.POST['username'])
        print(request.POST['email'])
        print(request.POST['address'])
        print(request.POST['address2'])
        print(request.POST['postalcode'])
        print(request.POST['bcompanyname'])
        print(request.POST['bfirstName'])
        print(request.POST['blastName'])
        print(request.POST[' busername'])
        print(request.POST['bemail'])
        print(request.POST['baddress'])
        print(request.POST['baddress2'])
        print(request.POST['bcountry'])
        print(request.POST['bprovince'])
        print(request.POST['bpostalcode'])

        PersonAccount = Person.objects.filter(user=request.user).first()
        CompanyAccountPerson = CompanyPerson.objects.filter(person=PersonAccount).first()
        CompanyAccount = Company.objects.filter(id=CompanyAccountPerson.company.id).first()
        CompanyInspection = Inspection.objects.all()  # filter(company=CompanyAccount)

        return render(request, 'accounts/clienthome.html',
                      {'inspections': CompanyInspection, 'company': CompanyAccount, 'person': PersonAccount})

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
