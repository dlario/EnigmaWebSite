from django.db import models
from django.contrib.auth.models import User, Group
from equipment.models import Equipment
from accounts.models import Company
from accounts.models import Person

class Inspection(models.Model):
    department = models.CharField(max_length=255, default="Inspection", choices = [('Inspection', 'Inspection'), ('Engineering', 'Engineering')])
    project_type = models.CharField(max_length=255, default="Inspection", choices = [('Equipment Inspection', 'Equipment Inspection'), ('Engineering Design', 'Engineering Design')])
    province = models.CharField(max_length=255, default="Alberta", choices = [('Alberta', 'Alberta'), ('British Columbia', 'British Columbia'), ('Manitoba', 'Manitoba')])
    title = models.CharField(max_length=255, default="Inspection of")
    project_number = models.CharField(max_length=255, default="AE218")
    client = models.ForeignKey(Company,related_name="client", on_delete=models.CASCADE)
    owner = models.ForeignKey(Company,related_name="owner", on_delete=models.CASCADE)
    project_supervisor = models.ForeignKey(Person,related_name="supervisor", on_delete=models.CASCADE)
    client_contact = models.ForeignKey(Person,related_name="client_contact", on_delete=models.CASCADE)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    project_terms = models.CharField(max_length=255, default="Lump Sum", choices = [('Lump Sum', 'Lump Sum'), ('Monthly', 'Monthly')])
    purchase_order = models.CharField(max_length=255, default="PO")
    status = models.CharField(max_length=255, default="Active", choices = [('Active', 'Active'), ('Not Started', 'Not Started'), ('Completed', 'Completed')])
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_number + " " + self.title

    class Meta:
      verbose_name = 'Inspection'
      verbose_name_plural = 'Inspections'
      ordering = ['-id']

class InspectionImage(models.Model):
    inspection_image = models.ForeignKey(Inspection,related_name="image", on_delete=models.CASCADE)
    description =  models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

class InspectionDocument(models.Model):
    inspection_document = models.ForeignKey(Inspection, related_name="document", on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    image = models.FileField(upload_to='images/')
