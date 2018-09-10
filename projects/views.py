from django.utils import timezone, html
from django.views.generic import FormView, TemplateView, ListView
from django_tables2 import RequestConfig, SingleTableView, Table, LinkColumn, Column, CheckBoxColumn, FileColumn, TemplateColumn
from django_tables2.utils import A
from django.utils.html import format_html
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from popupcrud.views import PopupCrudViewSet
from popupcrud.widgets import RelatedFieldPopupFormWidget
from django_select2.forms import Select2Widget

from .forms import ProjectForm
from .models import Project
from .filters import ProjectFilter
from equipment.models import Equipment
from accounts.models import Company, Person


# Create your views here.
class ProjectCrudViewset(PopupCrudViewSet):
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


class MainView(FormView):
    template_name = 'projects/create.html'
    form_class = Project
