from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import FormView
from projects.models import Project
from projects.filters import ProjectTitleFilter

from accounts.models import Person, CompanyPerson, Company
from accounts.forms import PersonForm, CompanyForm

from django.urls import reverse_lazy, reverse
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Q

from popupcrud.views import PopupCrudViewSet
from django.db.models.functions import TruncMonth, TruncYear

class personview(FormView):
    template_name = 'accounts/persondetails.html'
    form_class = PersonForm


class PersonCRUDViewSet(PopupCrudViewSet):
    model = Person
    app_name = 'accounts'

    form_class = PersonForm
    list_display = ('first_name', 'middle_name', 'last_name')
    list_url = reverse_lazy("accounts:authors")
    new_url = reverse_lazy("accounts:new-author")
    legacy_crud = False

    """
    form_class = AuthorForm
    list_permission_required = ('library.add_author',)
    create_permission_required = ('library.add_author',)
    update_permission_required = ('library.change_author',)
    delete_permission_required = ('library.delete_author',)
    """

    # Custom Attributes
    #    def half_age(self, author):  # pylint: disable=R0201
    #        return author.age / 2 if author.age else '-'

    #    half_age.label = "Half life"
    #    half_age.order_field = 'age'''

    def get_edit_url(self, obj):
        return reverse_lazy("account:edit-person", kwargs={'pk': obj.pk})

    def get_delete_url(self, obj):
        # Locking
        # if not obj.age or obj.age < 18:
        #    return None
        return reverse_lazy("account:delete-person", kwargs={'pk': obj.pk})


def person_list(request):
    persons = Person.objects.all()
    return render(request, 'persons/includes/partial_person_create.html', {'persons': persons})


def save_person_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            persons = Person.objects.all()
            data['html_person_list'] = render_to_string('persons/includes/partial_person_list.html', {
                'persons': persons
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
    else:
        form = PersonForm()
    return save_person_form(request, form, 'persons/includes/partial_person_create.html')


def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
    else:
        form = PersonForm(instance=person)
    return save_person_form(request, form, 'persons/includes/partial_person_update.html')


def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    data = dict()
    if request.method == 'POST':
        person.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        persons = Person.objects.all()
        data['html_person_list'] = render_to_string('persons/includes/partial_person_list.html', {
            'persons': persons
        })
    else:
        context = {'person': person}
        data['html_form'] = render_to_string('persons/includes/partial_person_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


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


class CompanyCRUDViewSet(PopupCrudViewSet):
    model = Company
    app_name = 'accounts'

    form_class = CompanyForm
    list_display = ('first_name', 'middle_name', 'last_name')
    list_url = reverse_lazy("accounts:authors")
    new_url = reverse_lazy("accounts:new-author")
    legacy_crud = False

    """
    form_class = AuthorForm
    list_permission_required = ('library.add_author',)
    create_permission_required = ('library.add_author',)
    update_permission_required = ('library.change_author',)
    delete_permission_required = ('library.delete_author',)
    """

    # Custom Attributes
    #    def half_age(self, author):  # pylint: disable=R0201
    #        return author.age / 2 if author.age else '-'

    #    half_age.label = "Half life"
    #    half_age.order_field = 'age'''

    def get_edit_url(self, obj):
        return reverse_lazy("account:edit-person", kwargs={'pk': obj.pk})

    def get_delete_url(self, obj):
        # Locking
        # if not obj.age or obj.age < 18:
        #    return None
        return reverse_lazy("account:delete-person", kwargs={'pk': obj.pk})


def companydetails(request):
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

        # TODO: Create a database recording changes in tranactions. Have the server know which ones were updated
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
        # CompanyAccount.city = request.POST.get('firstname')
        CompanyAccount.province = request.POST.get('province')
        CompanyAccount.address = request.POST.get('address')
        CompanyAccount.box_number = request.POST.get('firstname')
        CompanyAccount.postal_code = request.POST.get('postalcode')

        CompanyInspection = Project.objects.all()  # filter(company=CompanyAccount)

        if CompanyAccount:
            return render(request, 'accounts/companyhome.html',
                          {'inspections': CompanyInspection, 'company': CompanyAccount, 'person': PersonAccount})
        else:
            print("fail")
    else:
        UserDate = request.user
        PersonAccount = Person.objects.filter(user=request.user).first()
        CompanyAccountPerson = CompanyPerson.objects.filter(person=PersonAccount).first()
        CompanyAccount = Company.objects.filter(id=CompanyAccountPerson.company.id).first()

        return render(request, 'accounts/companydetails.html', {'company': CompanyAccount, 'person': PersonAccount})


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
        CompanyInspection = Project.objects.all()  # filter(company=CompanyAccount)

        return render(request, 'accounts/companyhome.html',
                      {'inspections': CompanyInspection, 'company': CompanyAccount, 'person': PersonAccount})


def companyhome(request):
    PersonAccount = Person.objects.filter(user=request.user).first()
    CompanyAccountPerson = CompanyPerson.objects.filter(person=PersonAccount).first()

    CompanyAccount = Company.objects.filter(id=CompanyAccountPerson.company.id).first()

    CompanyPersonnel = CompanyPerson.objects.filter(id=CompanyAccount.id).all()

    AdminStatus = True

    if AdminStatus:
        CompanyList = Company.objects.all().order_by("company_name")
        Projects = Project.objects.all()  # filter(company=CompanyAccount)
        CompanyInspection = ProjectTitleFilter(request.GET, queryset=Projects)
    else:
        CompanyList = None
        Projects = Project.objects.filter(Q(client=CompanyAccount.id) | Q(owner=CompanyAccount.id))

    CompanyInspection = ProjectTitleFilter(request.GET, queryset=Projects)

    return render(request, 'accounts/companyhome.html', {'company': CompanyAccount,
                                                         'companylist': CompanyList,
                                                         'admin': AdminStatus,
                                                         'person': PersonAccount,
                                                         'employee': CompanyPersonnel,
                                                         'filter': CompanyInspection,
                                                         'inspections': CompanyInspection})

def companyhome2(request, company_id=None):
    PersonAccount = Person.objects.filter(user=request.user).first()
    CompanyAccountPerson = CompanyPerson.objects.filter(person=PersonAccount).first()

    if company_id is None:
        CompanyAccount = Company.objects.filter(id=CompanyAccountPerson.company.id).first()
    else:
        CompanyAccount = Company.objects.filter(id=company_id).first()

    CompanyPersonnel = CompanyPerson.objects.filter(id=CompanyAccount.id).all()

    Projects = Project.objects.filter(Q(client=company_id) | Q(owner=company_id))

    CompanyInspection = ProjectTitleFilter(request.GET, queryset=Projects)

    AdminStatus = True

    if AdminStatus:
        CompanyList = Company.objects.all().order_by("company_name")
    else:
        CompanyList = None

    return render(request, 'accounts/companyhome.html', {'company': CompanyAccount,
                                                         'companylist': CompanyList,
                                                         'admin': AdminStatus,
                                                         'person': PersonAccount,
                                                         'employee': CompanyPersonnel,
                                                         'filter': CompanyInspection,
                                                         'inspections': CompanyInspection})

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])

        PersonAccount = Person.objects.filter(user=user).first()
        CompanyAccountPerson = CompanyPerson.objects.filter(person=PersonAccount).first()

        if user is not None:
            auth.login(request, user)
            # todo bounce to company new page if no company exists with name
            if CompanyAccountPerson:
                return redirect('companyhome')
            else:
                return redirect('companydetails')

        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')


class PersonViewSet(PopupCrudViewSet):
    model = Person
    form_class = PersonForm
    # fields = ('first_name', 'middle_name', 'last_name')
    list_display = ('first_name', 'middle_name', 'last_name')
    list_url = reverse_lazy("accounts:person:list")
    new_url = reverse_lazy("accounts:person:create")

    def get_edit_url(self, obj):
        return reverse("accounts:person:edit", kwargs={'pk': obj.pk})

    def get_delete_url(self, obj):
        return reverse("accounts:person:delete", kwargs={'pk': obj.pk})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('navhome')
