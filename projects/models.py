from django.db import models
from django.contrib.auth.models import User, Group
from equipment.models import Equipment
from accounts.models import Company, Person, CompanyPerson

class Project(models.Model):
    server_bt_id = models.IntegerField(default=None, blank=True, null=True)
    department = models.CharField(max_length=255, default="Engineering", choices = [('Inspection', 'Inspection'), ('Engineering', 'Engineering')])
    project_type = models.CharField(max_length=255, default="Engineering Design", choices = [('Equipment Inspection', 'Equipment Inspection'), ('Engineering Design', 'Engineering Design')])
    province = models.CharField(max_length=255, default="Alberta", choices = [('Alberta', 'Alberta'), ('British Columbia', 'British Columbia'), ('Manitoba', 'Manitoba')])
    title = models.CharField(max_length=255, default="Inspection of")
    project_number = models.CharField(max_length=255, default="AE218")
    client = models.ForeignKey(Company,related_name="project_client", on_delete=models.CASCADE)
    owner = models.ForeignKey(Company,related_name="project_owner", on_delete=models.CASCADE)
    project_supervisor = models.ForeignKey(Person,related_name="project_supervisor", on_delete=models.CASCADE)
    client_contact = models.ForeignKey(Person,related_name="proejct_client_contact", on_delete=models.CASCADE)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    project_terms = models.CharField(max_length=255, default="Lump Sum", choices = [('Lump Sum', 'Lump Sum'), ('Monthly', 'Monthly')])
    purchase_order = models.CharField(max_length=255, default="PO")
    status = models.CharField(max_length=255, default="Active", choices = [('Active', 'Active'), ('Not Started', 'Not Started'), ('Completed', 'Completed')])
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_number + " " + self.title

    class Meta:
      verbose_name = 'Project'
      verbose_name_plural = 'Projects'
      ordering = ['-id']