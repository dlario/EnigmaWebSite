from django.db import models
from django.contrib.auth.models import User, Group
from equipment.models import Equipment
from accounts.models import Company, Person, CompanyPerson
from website.models import lstPhase, lsttaskcategory, lsttaskdescription, lsttaskdetail, lstunit, lstdocumentgroup, lstRoles
from filer.fields.image import FilerImageField


class Project(models.Model):
    server_bt_id = models.IntegerField(default=None, blank=True, null=True)
    department = models.CharField(blank=True, null=True, max_length=255, default="Engineering", choices = [('Inspection', 'Inspection'), ('Engineering', 'Engineering')])
    project_type = models.CharField(blank=True, null=True, max_length=255, default="Engineering Design", choices = [('Equipment Inspection', 'Equipment Inspection'), ('Engineering Design', 'Engineering Design')])
    province = models.CharField(blank=True, null=True, max_length=255, default="Alberta", choices = [('Alberta', 'Alberta'), ('British Columbia', 'British Columbia'), ('Manitoba', 'Manitoba')])
    title = models.CharField(blank=True, null=True, max_length=255, default="Inspection of")
    project_number = models.CharField(blank=True, null=True, max_length=255, default="AE218")
    client = models.ForeignKey(Company,related_name="project_client",blank=True, null=True,  on_delete=models.CASCADE)
    owner = models.ForeignKey(Company,related_name="project_owner",blank=True, null=True,  on_delete=models.CASCADE)
    project_supervisor = models.ForeignKey(Person,related_name="project_supervisor", blank=True, null=True, on_delete=models.CASCADE)
    client_contact = models.ForeignKey(Person,related_name="project_client_contact", on_delete=models.CASCADE)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    project_terms = models.CharField(blank=True, null=True, max_length=255, default="Lump Sum", choices = [('Lump Sum', 'Lump Sum'), ('Monthly', 'Monthly')])
    purchase_order = models.CharField(blank=True, null=True, max_length=255, default="PO")
    status = models.CharField(blank=True, null=True, max_length=255, default="Active", choices = [('Active', 'Active'), ('Not Started', 'Not Started'), ('Completed', 'Completed')])
    equipment = models.ForeignKey(Equipment, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_number + " " + self.title

    class Meta:
      verbose_name = 'Project'
      verbose_name_plural = 'Projects'
      ordering = ['-id']


class ProjectTasks(models.Model):
    server_id = models.IntegerField(blank=True)
    project = models.ForeignKey(Project, related_name="task_project", blank=True, null=True, on_delete=models.CASCADE)
    parenttask = models.IntegerField(blank=True)
    title =  models.CharField(blank=True, null=True, max_length=255)
    level = models.IntegerField(blank=True)
    phase = models.ForeignKey(lstPhase,related_name="project_phase", blank=True, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(lsttaskcategory,related_name="project_category", blank=True, null=True, on_delete=models.CASCADE)
    description = models.ForeignKey(lsttaskdescription,related_name="project_description",blank=True, null=True,  on_delete=models.CASCADE)
    detail = models.ForeignKey(lsttaskdetail,related_name="project_detail", blank=True, null=True, on_delete=models.CASCADE)
    resource = models.ForeignKey(Person,related_name="project_resource", blank=True, null=True, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=4, blank=True, null=True, decimal_places=2)
    rateunits = models.ForeignKey(lstunit,related_name="project_rateunits", blank=True, null=True, on_delete=models.CASCADE)
    esthours = models.DecimalField(max_digits=4, blank=True, null=True, decimal_places=2)
    acthours = models.DecimalField(max_digits=4,blank=True, null=True, decimal_places=2)
    comments = models.CharField(max_length=255, blank=True)
    permission = models.CharField(max_length=255, blank=True)


class ProjectRoles(models.Model):
    server_id = models.IntegerField(blank=True)
    project = models.ForeignKey(Project,related_name="role_project", blank=True, null=True, on_delete=models.CASCADE)
    person = models.ForeignKey(Person,related_name="role_person", blank=True, null=True, on_delete=models.CASCADE)
    role = models.ForeignKey(lstRoles,related_name="role_role", blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('project',)
        verbose_name = "ProjectRole"
        verbose_name_plural = "ProjectRoles"

    def __str__(self):
        return self.role

class ProjectMilestone(models.Model):
    server_id = models.IntegerField(blank=True)
    project = models.ForeignKey(Project,related_name="milestone_project", blank=True, null=True, on_delete=models.CASCADE)
    #milestone = models.ForeignKey(lstMilestones, related_name="milestone_milestone", blank=True, null=True, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    date_completed = models.DateField(blank=True)


class ProjectTask(models.Model):
    server_id = models.IntegerField(blank=True)
    project = models.ForeignKey(Project,related_name="projecttask_project", blank=True, null=True, on_delete=models.CASCADE)
    task = models.ForeignKey(ProjectTasks,related_name="projecttask_task", blank=True, null=True, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    date_completed = models.DateField(blank=True)



class ProjectDocumentGroup(models.Model):
    server_id = models.IntegerField(blank=True)
    project = models.ForeignKey(Project,related_name="PDG_project", blank=True, null=True, on_delete=models.CASCADE)
    group = models.ForeignKey(lstdocumentgroup,related_name="PDG_group", blank=True, null=True, on_delete=models.CASCADE)
    order = models.IntegerField(blank=True)


class ProjectDocument(models.Model):
    project = models.ForeignKey(Project, related_name="projectdocument_project", blank=True, null=True, on_delete=models.CASCADE)
    group = models.ForeignKey(ProjectDocumentGroup, related_name="projectdocument_group", blank=True, null=True, on_delete=models.CASCADE)
    description = models.CharField(blank=True, null=True, max_length=255)
    document = models.FileField(blank=True, null=True, upload_to='images/')
    permission = models.CharField(blank=True, null=True, max_length=255, default="{}")
    #document2 = FilerImageField(blank=True, null=True,
    #                       related_name="document2")

#class ProjectActivity(models.Model):
#    Server_id = models.IntegerField()
#    ParentTask = models.IntegerField()


#class ProjectActivity(models.Model):
#    Server_id = models.IntegerField()
#    ParentTask = models.IntegerField()