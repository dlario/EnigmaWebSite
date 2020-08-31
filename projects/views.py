from django.utils import timezone, html
from django.views.generic import FormView, TemplateView, ListView
from django_tables2 import RequestConfig, SingleTableView, Table, LinkColumn, Column, CheckBoxColumn, FileColumn, \
    TemplateColumn
from django_tables2.paginators import LazyPaginator

from django_tables2.utils import A
from django.utils.html import format_html
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.db.models import Q
from django.views.generic import TemplateView
from django_popup_view_field.registry import registry_popup_view

from popupcrud.views import PopupCrudViewSet
from popupcrud.widgets import RelatedFieldPopupFormWidget
from django_select2.forms import Select2Widget

from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape

from inspections.forms import InspectionForm

from .forms import ProjectForm, ProjectLookupFormHelper, ProjectFilterFormHelper, CreditCardForm, \
    ProjectMilestone_Form, ProjectRole_Form, ColorForm, Address
from .models import Project, ProjectTasks, ProjectRoles, ProjectMilestone, ProjectDocumentGroup, ProjectDocument
from .filters import ProjectFilter
from equipment.models import Equipment
from accounts.models import Company, Person


# Create your views here.
class ProjectCRUDViewSet(PopupCrudViewSet):
    model = Project
    form_class = ProjectForm
    app_name = 'projects'
    list_display = ('title', 'author')
    list_url = reverse_lazy("library:books")
    new_url = reverse_lazy("library:new-book")
    # paginate_by = None # disable pagination
    related_object_popups = {
        'author': reverse_lazy("library:new-author")
    }
    legacy_crud = False

    item_actions = [
        ('Approve', 'far fa-thumbs-up', 'approve')
    ]
    empty_list_icon = 'fas fa-book'
    empty_list_message = 'You have no project.<br/>Create a book to get started.'

    @staticmethod
    def get_edit_url(obj):
        return reverse_lazy("project:edit-project", kwargs={'pk': obj.pk})

    @staticmethod
    def get_delete_url(obj):
        return reverse_lazy("project:delete-project", kwargs={'pk': obj.pk})

    @staticmethod
    def get_detail_url(obj):
        return reverse_lazy("project:detail-project", kwargs={'pk': obj.pk})

    def approve(self, request, item_or_list):  # pylint: disable=R0201
        return True, "Request has been approved"


class ProjectRoleCrudViewset(PopupCrudViewSet):
    model = ProjectRoles
    form_class = ProjectRole_Form
    app_name = 'projects'
    list_display = ('project', 'person', 'role')
    list_url = reverse_lazy("projects:roles")
    new_url = reverse_lazy("projects:new-role")
    # paginate_by = None # disable pagination
    related_object_popups = {
        'role': reverse_lazy("library:new-role")
    }
    legacy_crud = False

    item_actions = [
        ('Approve', 'far fa-thumbs-up', 'approve')
    ]
    empty_list_icon = 'fas fa-book'
    empty_list_message = 'You have no roles assigned to this project.<br/>Create a role to get started.'

    @staticmethod
    def get_edit_url(obj):
        return reverse_lazy("projects:edit-role", kwargs={'pk': obj.pk})

    @staticmethod
    def get_delete_url(obj):
        return reverse_lazy("projects:delete-role", kwargs={'pk': obj.pk})

    @staticmethod
    def get_detail_url(obj):
        return reverse_lazy("projects:detail-role", kwargs={'pk': obj.pk})

    def approve(self, request, item_or_list):  # pylint: disable=R0201
        return True, "Request has been approved"


class MainView(FormView):
    template_name = 'projects/create.html'
    form_class = Project


class BookView(FormView):
    template_name = 'inspections/bookinspection.html'
    form_class = InspectionForm


class InspectionTable(Table):
    def render_name(self, value, record):
        # url = record.get_absolute_url()
        url = "/services/engineering"
        edit_entries = TemplateColumn('<a href="/inspection/detail/{{record.id}}">Edit</a>')
        return html.mark_safe('<a href="%s">%s</a>' % (url, record))

    class Meta:
        model = Project
        name = LinkColumn('project_number2',
                          text='static text',
                          attrs={'a': {'style': 'color: red;'}}
                          )
        fields = ['project_number', 'title', 'owner']
        # template_name = 'django_tables2/table.html'
        # template_name = 'django_tables2/bootstrap4.html'
        template_name = 'django_tables2/bootstrap-responsive.html'
        # template_name = 'django_tables2/semantic.html'
        row_attrs = {
            'data-href': lambda record: record.pk,
            'href': '/services/engineering'
        }


class ImageColumn(Column):
    def render(self, value):
        return format_html('<img src="/media/img/{}.jpg" />', value)


class InspectionTableView(TemplateView):
    template_name = 'inspections/inspectionfiltertable.html'

    def get_queryset(self, **kwargs):
        return Project.objects.all()

    def get_context_data(self, **kwargs):
        context = super(InspectionTableView, self).get_context_data(**kwargs)
        filter = ProjectFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = ProjectFilterFormHelper()
        table = InspectionTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context


class InspectionListView(ListView):
    template_name = 'inspections/inspectionfiltertable.html'
    model = Project

    def get_queryset(self, **kwargs):
        return Project.objects.all()
        # return Project.objects.filter(taxon="Cheloniidae")

    def get_context_data(self, **kwargs):
        context = super(InspectionListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PagedFilteredTableView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'

    def get_queryset(self, **kwargs):
        qs = super(PagedFilteredTableView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_table(self, **kwargs):
        table = super(PagedFilteredTableView, self).get_table()
        RequestConfig(self.request, paginate={"per_page": self.paginate_by}).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(PagedFilteredTableView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context


def index(request):
    return render(request, 'inspections/index.html')


def projectlist(request):
    return render(request, 'inspections/projectlist.html')


def create(request):
    if request.method == 'POST':
        if request.POST['title']:
            newproject = Project()
            newproject.inspector = request.POST['title']
            newproject.department = request.POST['department']
            newproject.project_type = request.POST['project_type']
            newproject.province = request.POST['province']
            newproject.title = request.POST['title']
            newproject.project_number = request.POST['project_number']
            newproject.client = Company.objects.get(id=request.POST['client'])
            newproject.owner = Company.objects.get(id=request.POST['owner'])
            newproject.project_supervisor = Person.objects.get(id=request.POST['project_supervisor'])
            newproject.client_contact = Person.objects.get(id=request.POST['client_contact'])
            newproject.start_date = timezone.datetime.now()
            newproject.end_date = request.POST['end_date']
            newproject.project_terms = request.POST['project_terms']
            newproject.purchase_order = request.POST['purchase_order']
            newproject.status = request.POST['status']
            newproject.equipment = Equipment.objects.get(id=request.POST['equipment'])
            newproject.createdby = request.user

            newproject.save()
            # return redirect('/inspections/' + str(inspection.id))
            return render(request, 'projects/companyprojects.html')
        else:
            return render(request, 'projects/companyprojects.html')
    else:
        return render(request, 'projects/companyprojects.html')


def projects(request):
    projects = Project.objects
    return render(request, 'projects/companyprojects.html', {'projects': projects})


@login_required(login_url="/accounts/signup")
def detail(request, project_id, project_number):
    project = get_object_or_404(Project, pk=project_id)

    model = Project
    table_class = ProjectTable
    paginate_by = 5
    filter_class = ProjectFilter
    formhelper_class = ProjectFilterFormHelper
    projecthelper_class = ProjectLookupFormHelper
    table = ProjectTable(Project.objects.all())  # Works
    table = PagedFilteredTableView  # Works
    pagination_class = LazyPaginator

    if hasattr(project, 'project_supervisor.first_name') and hasattr(project, 'project_supervisor.last_name'):
        projectlead = project.project_supervisor.first_name + " " + project.project_supervisor.last_name
    else:
        projectlead = None

    if hasattr(project, 'client_contact.first_name') and hasattr(project, 'client_contact.last_name'):
        clientcontact = project.client_contact.first_name + " " + project.client_contact.last_name
    else:
        clientcontact = None

    if hasattr(project, 'owner.company_name'):
        owner = project.owner.company_name
    else:
        owner = None

    if hasattr(project, 'client.company_name'):
        consignee = project.client.company_name
    else:
        consignee = None

    firstformset = ProjectRole_Form()
    secondformset = ProjectMilestone_Form()

    mainimage = ProjectDocument.objects.filter(project_id=project_id).first()
    tasks = ProjectTasks.objects.filter(project_id=project_id).all()
    roles = ProjectRoles.objects.filter(project_id=project_id).first()
    milestones = ProjectMilestone.objects.filter(project_id=project_id).first()
    documentgroup = ProjectDocumentGroup.objects.filter(project_id=project_id).first()
    documents = ProjectDocument.objects.filter(project_id=project_id).first()

    person = Person.objects.filter()
    if project:
        return render(request, 'projects/detail.html', {'project': project,
                                                        'mainimage': mainimage,
                                                        'projectlead': projectlead,
                                                        'clientcontact': clientcontact,
                                                        'owner': owner,
                                                        'consignee': consignee,
                                                        'tasks': tasks,
                                                        'roles': roles,
                                                        'milestones': milestones,
                                                        'documentgroup': documentgroup,
                                                        'documents': documents,
                                                        'projectrole': firstformset,
                                                        'table': table})
    else:
        return render(request, 'projects/inspections.html')


class ProjectTable(Table):
    def render_name(self, value, record):
        # url = record.get_absolute_url()
        url = "/services/engineering"
        edit_entries = TemplateColumn('<a href="/project/detail/{{record.id}}">Edit</a>')
        return html.mark_safe('<a href="%s">%s</a>' % (url, record))

    class Meta:
        model = Project
        name = LinkColumn('project_number2',
                          text='static text',
                          attrs={'a': {'style': 'color: red;'}}
                          )
        fields = ['project_number', 'title', 'owner']
        # template_name = 'django_tables2/table.html'
        # template_name = 'django_tables2/bootstrap4.html'
        template_name = 'django_tables2/bootstrap-responsive.html'
        # template_name = 'django_tables2/semantic.html'
        row_attrs = {
            'data-href': lambda record: record.pk,
            'href': '/services/engineering'
        }


class ProjectTableView(TemplateView):
    template_name = 'projects/projectfiltertable.html'

    def get_queryset(self, **kwargs):
        return Project.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProjectTableView, self).get_context_data(**kwargs)
        filter = ProjectFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = ProjectFilterFormHelper()
        table = ProjectTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context


class ProjectListView(ListView):
    template_name = 'projects/projectfiltertable.html'
    model = Project

    def get_queryset(self, **kwargs):
        return Project.objects.all()
        # return Inspection.objects.filter(taxon="Cheloniidae")

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def uploadfiles(request):
    if request.method == 'POST':
        new_file = ProjectDocument()

        project = get_object_or_404(Project, pk=request.POST['project_id'])
        new_file.project_id = request.POST['project_id']
        new_file.document = request.FILES['file']
        # new_file.group = group_id
        new_file.description = request.POST['description']
        # new_file.permission = permission
        new_file.save()

        return HttpResponseRedirect(reverse('detail', args=[new_file.project_id, project.project_number]))

    # return render('detail', {'project_id':'new_file.project_id'})


@login_required(login_url="/accounts/signup")
def bookinspection(request, equipment_id):
    if request.method == 'POST':
        product = get_object_or_404(Project, pk=equipment_id)
        product.save()
        return redirect('/equipment/' + str(equipment_id))


def inspectiondocuments(request, pk):
    inspections = Project.objects
    return render(request, 'inspections/inspectiondocumentimport.html')  # , {'inspections':inspections})


class FooTableView(PagedFilteredTableView):
    model = Project
    table_class = InspectionTable
    paginate_by = 5
    filter_class = ProjectFilter
    formhelper_class = ProjectFilterFormHelper
    search_class = CreditCardForm
    projecthelper_class = ProjectLookupFormHelper
    template_name = 'projects/projectfiltertable.html'

class OrderListJson(BaseDatatableView):
    #datatable-list-view
    # The model we're going to show
    model = Project

    # define the columns that will be returned
    columns = ['project_number', 'title', 'owner']
    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non sortable columns use empty
    # value like ''
    order_columns = ['project_number', 'title', 'owner']

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 50

    def render_column(self, row, column):
        # We want to render user as a custom column
        if column == 'user':
            # escape HTML for security reasons
            return escape('{0} {1}'.format(row.owner, row.client))
        else:
            return super(OrderListJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(name__istartswith=search)

        # more advanced example using extra parameters
        filter_customer = self.request.GET.get('owner', None)

        if filter_customer:
            customer_parts = filter_customer.split(' ')
            qs_params = None
            for part in customer_parts:
                q = Q(Owner__istartswith=part)|Q(client__istartswith=part)
                qs_params = qs_params | q if qs_params else q
            qs = qs.filter(qs_params)
        return qs

class ColorFormView(FormView):
    template_name = "projects/color_form.html"
    form_class = ColorForm

    def form_valid(self, form):
        color = form.cleaned_data.get("color")
        return HttpResponse("Your color: {0}".format(color))