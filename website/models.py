from django.db import models
from accounts.models import Company, Person, CompanyPerson
from equipment.models import Equipment


class lstRoles(models.Model):
    role = models.CharField(blank=True, null=True, max_length=255)


class lstMilestones(models.Model):
    milestone = models.CharField(blank=True, null=True, max_length=255)


class lstPhase(models.Model):
    Phase = models.CharField(blank=True, null=True, max_length=255)


class lstDocumentTypes(models.Model):
    DocumentType = models.CharField(blank=True, null=True, max_length=255)


class lstdocumentgroup(models.Model):
    DocumentType = models.CharField(blank=True, null=True, max_length=255)


class lsttaskcategory(models.Model):
    Name_id = models.IntegerField(blank=True, null=True)
    Name = models.IntegerField(blank=True, null=True)
    NameText = models.CharField(blank=True, null=True, max_length=255)
    Abbr = models.CharField(blank=True, null=True, max_length=255)


class lsttaskrelation(models.Model):
    Server_id = models.IntegerField(blank=True, null=True, )
    Name = models.IntegerField(blank=True, null=True, )
    NameText = models.CharField(blank=True, null=True, max_length=255)


class lsttaskdescription(models.Model):
    Server_id = models.IntegerField(blank=True, null=True)
    Name = models.IntegerField(blank=True, null=True, )
    NameText = models.CharField(blank=True, null=True, max_length=255)
    Abbr = models.CharField(blank=True, null=True, max_length=255)


class lsttaskdetail(models.Model):
    Server_id = models.IntegerField(blank=True, null=True)
    Name = models.IntegerField(blank=True, null=True)
    NameText = models.CharField(blank=True, null=True, max_length=255)
    Abbr = models.CharField(blank=True, null=True, max_length=255)


class lstunittype(models.Model):
    Server_id = models.IntegerField(blank=True, null=True, )
    Name = models.IntegerField(blank=True, null=True, )
    NameText = models.CharField(blank=True, null=True, max_length=255)


class lstunit(models.Model):
    Server_id = models.IntegerField(blank=True, null=True)
    Name = models.IntegerField(blank=True, null=True)
    Type_id = models.ForeignKey(lstunittype, related_name="unittype", blank=True, null=True, on_delete=models.CASCADE)
    NameText = models.CharField(blank=True, null=True, max_length=255)


class lstcountry(models.Model):
    Server_id = models.IntegerField(blank=True, null=True)
    Name = models.IntegerField(blank=True, null=True)
    NameText = models.CharField(blank=True, null=True, max_length=255)


class lstcity(models.Model):
    Server_id = models.IntegerField(blank=True, null=True)
    Name = models.IntegerField(blank=True, null=True)
    NameText = models.CharField(blank=True, null=True, max_length=255)


class lstaogtype(models.Model):
    Server_id = models.IntegerField(blank=True, null=True, )
    Name = models.IntegerField(blank=True, null=True, )
    NameText = models.CharField(blank=True, null=True, max_length=255)


class btareaofgovernance(models.Model):
    Server_id = models.IntegerField(blank=True, null=True)
    Title = models.CharField(blank=True, null=True, max_length=255)
    AttributeCount = models.IntegerField(blank=True, null=True, )


class lstmunicipalitytype(models.Model):
    Server_id = models.IntegerField(blank=True, null=True)
    Name = models.IntegerField(blank=True, null=True)
    NameText = models.CharField(blank=True, null=True, max_length=255)


class lstmunicipality(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)


class lstcontacttype(models.Model):
    Server_id = models.IntegerField(blank=True, null=True)
    Name = models.IntegerField(blank=True, null=True)
    NameText = models.CharField(blank=True, null=True, max_length=255)


class lstnameprefix(models.Model):
    Server_id = models.IntegerField(blank=True, null=True, )
    Name = models.IntegerField(blank=True, null=True, )
    NameText = models.CharField(blank=True, null=True, max_length=255)


class lstnamesuffix(models.Model):
    Server_id = models.IntegerField(blank=True, null=True)
    Name = models.IntegerField(blank=True, null=True)
    NameText = models.CharField(blank=True, null=True, max_length=255)


class lstprofession(models.Model):
    Server_id = models.IntegerField(blank=True, null=True)
    Name = models.IntegerField(blank=True, null=True)
    NameText = models.CharField(blank=True, null=True, max_length=255)


class lstprofessiondesignation(models.Model):
    Server_id = models.IntegerField(blank=True, null=True)
    Name = models.IntegerField(blank=True, null=True)
    NameText = models.CharField(blank=True, null=True, max_length=255)


class lstprofessionlevel(models.Model):
    Server_id = models.IntegerField(blank=True, null=True)
    Name = models.IntegerField(blank=True, null=True)
    NameText = models.CharField(blank=True, null=True, max_length=255)
