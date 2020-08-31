from django import forms
from django.urls import reverse_lazy, reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div
from crispy_forms.bootstrap import (
    PrependedText, AppendedText, PrependedAppendedText, FormActions)
from inspections.models import Inspection
from projects.models import Project, ProjectRoles
from accounts.models import Company, Person, CompanyPerson
from website.models import lstRoles#, lstMilestones
from django_select2.forms import Select2MultipleWidget


try:
    from django_select2.forms import Select2Widget

    _select2 = True
except ImportError:
    _select2 = False

from popupcrud.views import PopupCrudViewSet
from popupcrud.widgets import RelatedFieldPopupFormWidget

from django import forms
from django_popup_view_field.fields import PopupViewField
from .popups import ColorsPopupView

class ColorForm(forms.Form):

    color = PopupViewField(
        view_class=ColorsPopupView,
        popup_dialog_title='What is your favorite color',
        required=True,
        help_text='be honest'
    )

class ProjectForm(forms.ModelForm):
    # department = forms.ModelChoiceField(queryset=department.objects.all())
    class Meta:
        model = Inspection
        fields =['department',
                 'project_type',
                 'province',
                 'title',
                 'project_number',
                 'client',
                 'owner',
                 'project_supervisor',
                 'client_contact',
                 'start_date',
                 'end_date',
                 'project_terms',
                 'purchase_order',
                 'status',
                 'equipment']

    def __init__(self, *args, **kwargs):
        super(Project, self).__init__(*args, **kwargs)

    # Uni-form
    helper = FormHelper()
    helper.form_method = 'POST'
    #helper.form_id = 'id-project'
    #action = "{% url 'home' %}"
    helper.form_action = 'create'
    #helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Div(
            Div('department', css_class='col-md-6'),
            Div('project_type', css_class='col-md-6'), css_class='row'),
        'province',
        Div(Div('project_number', css_class='col-md-6'),
        Div('title', css_class='col-md-6'), css_class='row'),\
                    'client',\
                    'owner',\
                    'project_supervisor',\
                    'client_contact',\
                    'start_date',\
                    'end_date',\
                    'project_terms',\
                    'purchase_order',\
                    'status',\
                    'equipment',\
                    Submit('submit', 'Create Project', css_class="btn-primary"),\
                    Submit('cancel', 'Cancel'),
    )

class BookInspection(forms.ModelForm):
    # department = forms.ModelChoiceField(queryset=department.objects.all())
    class Meta:
        model = Inspection
        fields =['project_type',
                 'client',
                 'owner',
                 'client_contact',
                 'start_date',
                 'end_date',
                 'purchase_order',
                 'equipment']

    def __init__(self, *args, **kwargs):
        super(Project, self).__init__(*args, **kwargs)

    # Uni-form
    helper = FormHelper()
    helper.form_method = 'POST'
    #helper.form_id = 'id-project'
    #action = "{% url 'home' %}"
    helper.form_action = 'create'
    #helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Div(
            Div('project_type', css_class='col-md-6'), css_class='row'),
        Div( css_class='row'),\
                    'client',\
                    'owner',\
                    'client_contact',\
                    'start_date',\
                    'purchase_order',\
                    'equipment',\
                    Submit('submit', 'Create Project', css_class="btn-primary"),\
                    Submit('cancel', 'Cancel'),
    )


class ProjectForm(forms.Form):
    item = forms.CharField()
    quantity = forms.IntegerField(label="Qty")
    price = forms.DecimalField()


class ProjectRole_Form(forms.Form):
    person = forms.ModelMultipleChoiceField(queryset=Person.objects.all(), widget=Select2MultipleWidget)
    role = forms.ModelMultipleChoiceField(queryset=lstRoles.objects.all(), widget=Select2MultipleWidget)

    helper = FormHelper()
    helper.form_method = 'POST'
    #helper.form_id = 'id-project'
    #action = "{% url 'home' %}"
    helper.form_action = 'create'
    #helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Div(
            Div('person', css_class='col-md-6'),
            Div('role', css_class='col-md-6'), css_class='row'),
                    Submit('submit', 'Create Role', css_class="btn-primary"),\
                    Submit('cancel', 'Cancel'),
    )

class ProjectCrudViewset(PopupCrudViewSet):
    model = ProjectRoles
    form_class = ProjectRole_Form
    app_name = 'project'
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
    empty_list_message = 'You have not defined any books.<br/>Create a book to get started.'

    @staticmethod
    def get_edit_url(obj):
        return reverse_lazy("library:edit-book", kwargs={'pk': obj.pk})

    @staticmethod
    def get_delete_url(obj):
        return reverse_lazy("library:delete-book", kwargs={'pk': obj.pk})

    @staticmethod
    def get_detail_url(obj):
        return reverse_lazy("library:detail-book", kwargs={'pk': obj.pk})

    def approve(self, request, item_or_list):  # pylint: disable=R0201
        return True, "Request has been approved"

class ProjectRolesFormHelper(FormHelper):
    model = ProjectRoles
    form_method = 'POST'
    form_tag = False
    form_show_labels = False

class ProjectMilestone_Form(forms.Form):
    #milestone = forms.ModelMultipleChoiceField(queryset=lstMilestones.objects.all(), widget=Select2MultipleWidget)
    role = forms.ModelMultipleChoiceField(queryset=lstRoles.objects.all(), widget=Select2MultipleWidget)
    start_date = forms.DateField()
    end_date = forms.DateField()
    date_completed = forms.DateField()

    helper = FormHelper()
    helper.form_method = 'POST'
    # helper.form_id = 'id-project'
    # action = "{% url 'home' %}"
    helper.form_action = 'create'
    # helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Div(
            Div('milestone', css_class='col-md-6'),
            Div('role', css_class='col-md-6'), css_class='row'),
        'start_date', \
        'end_date',
        'date_completed',
        Submit('submit', 'Create Role', css_class="btn-primary"), \
        Submit('cancel', 'Cancel'),
    )


class ProjectDocument_Form(forms.Form):
    #milestone = forms.ModelMultipleChoiceField(queryset=lstMilestones.objects.all(), widget=Select2MultipleWidget)
    role = forms.ModelMultipleChoiceField(queryset=lstRoles.objects.all(), widget=Select2MultipleWidget)
    start_date = forms.DateField()
    end_date = forms.DateField()
    date_completed = forms.DateField()

    helper = FormHelper()
    helper.form_method = 'POST'
    # helper.form_id = 'id-project'
    # action = "{% url 'home' %}"
    helper.form_action = 'create'
    # helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Div(
            Div('milestone', css_class='col-md-6'),
            Div('role', css_class='col-md-6'), css_class='row'),
        'start_date', \
        'end_date',
        'date_completed',
        Submit('submit', 'Create Role', css_class="btn-primary"), \
        Submit('cancel', 'Cancel'),
    )

class ProjectTask_Form(forms.Form):
    #milestone = forms.ModelMultipleChoiceField(queryset=lstMilestones.objects.all(), widget=Select2MultipleWidget)
    role = forms.ModelMultipleChoiceField(queryset=lstRoles.objects.all(), widget=Select2MultipleWidget)
    start_date = forms.DateField()
    end_date = forms.DateField()
    date_completed = forms.DateField()

    helper = FormHelper()
    helper.form_method = 'POST'
    # helper.form_id = 'id-project'
    # action = "{% url 'home' %}"
    helper.form_action = 'create'
    # helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Div(
            Div('milestone', css_class='col-md-6'),
            Div('role', css_class='col-md-6'), css_class='row'),
        'start_date', \
        'end_date',
        'date_completed',
        Submit('submit', 'Create Role', css_class="btn-primary"), \
        Submit('cancel', 'Cancel'),
    )

class ProjectFilterFormHelper(FormHelper):
    model = Project
    form_method = 'GET'
    form_tag = False
    form_show_labels = False
    layout = Layout(
        Div(
            Div('project_number__contains', css_class='col-md-5'),
            Div('client', css_class='col-md-5'),
            Div(Submit('submit', 'Apply Filter'), css_class='col-md-2'), css_class='row'),)

class ProjectLookupFormHelper(FormHelper):
    model = Inspection
    form_method = 'GET'
    form_tag = False
    form_show_labels = False
    layout = Layout(
        Div(
            Div('project_number__contains', css_class='col-md-5'),
            Div(Submit('submit', 'Look Up Project'), css_class='col-md-2'), css_class='row'),)

class Address(forms.Form):
    # Wrapping the fields "housenumber and addition". Assign extra class to the fields

    Project_Number = forms.CharField()

    description = forms.CharField(
        widget=forms.Textarea(),
    )

    radio_buttons = forms.ChoiceField(
        choices=(
            ('option_one', "Option one is this and that be sure to include why it's great"),
            ('option_two', "Option two can is something else and selecting it will deselect option one")
        ),
        widget=forms.RadioSelect,
        initial='option_two',
    )

    checkboxes = forms.MultipleChoiceField(
        choices=(
            ('option_one', "Option one is this and that be sure to include why it's great"),
            ('option_two', 'Option two can also be checked and included in form results'),
            ('option_three', 'Option three can yes, you guessed it also be checked and included in form results')
        ),
        initial='option_one',
        widget=forms.CheckboxSelectMultiple,
        help_text="<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
    )

    appended_text = forms.CharField(
        help_text="Here's more help text"
    )

    prepended_text = forms.CharField()

    prepended_text_two = forms.CharField()

    multicolon_select = forms.MultipleChoiceField(
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
    )

    # Uni-form
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('Project_Number', css_class='input-xlarge'),
        Field('description', rows="3", css_class='input-xlarge'),
        'radio_buttons',

        AppendedText('appended_text', '.00'),
        PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">',
                      active=True),
        PrependedText('prepended_text_two', '@'),
        'multicolon_select',
        FormActions(
            Submit('submit', 'Create Project', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        )
    )

class CartForm(forms.Form):
    item = forms.CharField()
    quantity = forms.IntegerField(label="Qty")
    price = forms.DecimalField()

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.layout = Layout(
        'item',
        PrependedText('quantity', '#'),
        PrependedAppendedText('price', '$', '.00'),
        FormActions(Submit('login', 'login', css_class='btn-primary'))
    )

class CreditCardForm(forms.Form):
    fullname = forms.CharField(label="Full Name", required=True)
    card_number = forms.CharField(label="Card", required=True, max_length=16)
    expire = forms.DateField(label="Expire Date", input_formats=['%m/%y'])
    ccv = forms.IntegerField(label="ccv")
    notes = forms.CharField(label="Order Notes", widget=forms.Textarea())

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-4'
    helper.layout = Layout(
        Field('fullname', css_class='input-sm'),
        Field('card_number', css_class='input-sm'),
        Field('expire', css_class='input-sm'),
        Field('ccv', css_class='input-sm'),
        Field('notes', rows=3),
        FormActions(Submit('purchase', 'purchase', css_class='btn-primary'))
    )