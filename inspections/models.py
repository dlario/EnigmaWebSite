from django.db import models
from django.contrib.auth.models import User, Group
from equipment.models import Equipment
from accounts.models import Company
from accounts.models import Person
from website.models import *


class Inspection(models.Model):
    server_bt_id = models.IntegerField(default=None, blank=True, null=True)
    department = models.CharField(blank=True, null=True, max_length=255, default="Inspection", choices = [('Inspection', 'Inspection'), ('Engineering', 'Engineering')])
    project_type = models.CharField(blank=True, null=True, max_length=255, default="Inspection", choices = [('Equipment Inspection', 'Equipment Inspection'), ('Engineering Design', 'Engineering Design')])
    province = models.CharField(blank=True, null=True, max_length=255, default="Alberta", choices = [('Alberta', 'Alberta'), ('British Columbia', 'British Columbia'), ('Manitoba', 'Manitoba')])
    title = models.CharField(blank=True, null=True, max_length=255, default="Inspection of")
    project_number = models.CharField(blank=True, null=True, max_length=255, default="AE218")
    client = models.ForeignKey(Company,related_name="client", blank=True, null=True, on_delete=models.CASCADE)
    owner = models.ForeignKey(Company,related_name="owner", blank=True, null=True, on_delete=models.CASCADE)
    project_supervisor = models.ForeignKey(Person,related_name="supervisor", blank=True, null=True, on_delete=models.CASCADE)
    client_contact = models.ForeignKey(Person,related_name="client_contact", blank=True, null=True, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    project_terms = models.CharField(max_length=255, blank=True, null=True, default="Lump Sum", choices = [('Lump Sum', 'Lump Sum'), ('Monthly', 'Monthly')])
    purchase_order = models.CharField(max_length=255, blank=True, null=True, default="PO")
    status = models.CharField(max_length=255, blank=True, null=True, default="Active", choices = [('Active', 'Active'), ('Not Started', 'Not Started'), ('Completed', 'Completed')])
    equipment = models.ForeignKey(Equipment, blank=True, null=True, on_delete=models.CASCADE)
    permission = models.CharField(max_length=255, blank=True, null=True, default="{}")

    def __str__(self):
        return self.project_number + " " + self.title

    class Meta:
      verbose_name = 'Inspection'
      verbose_name_plural = 'Inspections'
      ordering = ['-id']


class InspectionImage(models.Model):
    inspection_image = models.ForeignKey(Inspection, related_name="image", blank=True, null=True, on_delete=models.CASCADE)
    description = models.CharField(blank=True, null=True, max_length=255)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    permission = models.CharField(blank=True, null=True, max_length=255, default="{}")


class InspectionDocument(models.Model):
    inspection_document = models.ForeignKey(Inspection, related_name="document", blank=True, null=True, on_delete=models.CASCADE)
    description = models.CharField(blank=True, null=True, max_length=255)
    document = models.FileField(blank=True, null=True, upload_to='images/')
    permission = models.CharField(blank=True, null=True, max_length=255, default="{}")