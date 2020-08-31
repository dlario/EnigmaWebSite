from django.db import models
from django.contrib.auth.models import User
from filer.fields.image import FilerImageField

class Person(models.Model):
    server_bt_id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(blank=True, null=True, max_length=255, default="")
    middle_name = models.CharField(blank=True, null=True, max_length=255, default="")
    last_name = models.CharField(blank=True, null=True,max_length=255, default="")
    photo = FilerImageField(blank=True, null=True, on_delete=models.CASCADE, related_name="person_photo")
    def __str__(self):
        return self.first_name + " " + self.last_name

class ContactInformation(models.Model):
    description = models.CharField(blank=True, null=True, max_length=255, default="")
    contact_type = models.CharField(blank=True, null=True, max_length=255, default="")
    contact = models.CharField(blank=True, null=True, max_length=255, default="")
    preferred = models.BooleanField(blank=True, null=True)
    person = models.ForeignKey(Person, blank=True, null=True, on_delete=models.CASCADE)

# Create your models here.
class Company(models.Model):
    server_bt_id = models.IntegerField(blank=True, null=True)
    company_name = models.CharField(blank=True, null=True, max_length=255, default="")
    city = models.CharField(blank=True, null=True, max_length=255, default="Grande Prairie")
    province = models.CharField(blank=True, null=True, max_length=255, default="Alberta")
    address = models.CharField(blank=True, null=True, max_length=255, default="")
    box_number = models.CharField(blank=True, null=True, max_length=255, default="")
    postal_code = models.CharField(blank=True, null=True, max_length=255, default="")
    logo = FilerImageField(blank=True, null=True, on_delete=models.CASCADE, related_name="logo_company")
    def __str__(self):
        return self.company_name + " (" + self.city + ")"


class CompanyPerson(models.Model):
    person = models.ForeignKey(Person, blank=True, null=True, on_delete=models.CASCADE)
    role = models.CharField(blank=True, null=True, max_length=255)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
    #companyadmin = models.BooleanField(default=0)

    def __str__(self):
        return self.person.__str__() + ": " + self.role

