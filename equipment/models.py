from django.db import models
#from inspections.models import Inspection
# Create your models here.


class Equipment(models.Model):
    server_bt_id = models.IntegerField(default=None, blank=True, null=True)
    equipment_category = models.CharField(blank=True, null=True, max_length=255, default="")
    equipment_subcategory = models.CharField(blank=True, null=True, max_length=255, default="")
    manufacturer = models.CharField(blank=True, null=True, max_length=255, default="")
    serial_number = models.CharField(blank=True, null=True, max_length=255, default="")
    model_number = models.CharField(blank=True, null=True, max_length=255, default="")
    #inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)

    def __str__(self):
        return self.manufacturer + " - " + self.model_number + " - " + self.serial_number


class lstequipmenttype(models.Model):
    Server_id = models.IntegerField(blank=True, null=True)
    Name = models.IntegerField(blank=True, null=True)
    NameText = models.CharField(blank=True, null=True, max_length=255)


class lstequipmentitem(models.Model):
    Server_id = models.IntegerField(blank=True, null=True)
    Name = models.IntegerField(blank=True)
    NameText = models.CharField(blank=True, null=True, max_length=255)


class lstequipmentinspectiontype(models.Model):
    Server_id = models.IntegerField(blank=True, null=True)
    Name = models.IntegerField(blank=True, null=True)
    NameText = models.CharField(blank=True, null=True, max_length=255)