from django.db import models
#from inspections.models import Inspection
# Create your models here.


class Equipment(models.Model):
    equipment_category = models.CharField(max_length=255, default="")
    equipment_subcategory = models.CharField(max_length=255, default="")
    manufacturer = models.CharField(max_length=255, default="")
    serial_number = models.CharField(max_length=255, default="")
    model_number = models.CharField(max_length=255, default="")
    #inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)

    def __str__(self):
        return self.manufacturer + " - " + self.model_number + " - " + self.serial_number