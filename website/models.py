from django.db import models
from accounts.models import Company, Person, CompanyPerson
from equipment.models import Equipment


class lstRoles(models.Model):
    role = models.CharField(max_length=255)


class lstPhase(models.Model):
    Phase = models.CharField(max_length=255)


class lstDocumentTypes(models.Model):
    DocumentType = models.CharField(max_length=255)


class lsttaskcategory(models.Model):
    Name_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)
    Abbr = models.CharField(max_length=255)


class lsttaskrelation(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)


class lsttaskdescription(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)
    Abbr = models.CharField(max_length=255)


class lsttaskdetail(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)
    Abbr = models.CharField(max_length=255)


class lstunittype(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)


class lstunit(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    Type_id = models.ForeignKey(lstunittype,related_name="unittype", on_delete=models.CASCADE)
    NameText = models.CharField(max_length=255)


class WorkTasks(models.Model):
    Server_id = models.IntegerField()
    ParentTask = models.IntegerField()
    Title =  models.CharField(max_length=255)
    Level = models.IntegerField()
    Phase = models.ForeignKey(lstPhase,related_name="phase", on_delete=models.CASCADE)
    Category = models.ForeignKey(lsttaskcategory,related_name="category", on_delete=models.CASCADE)
    Description = models.ForeignKey(lsttaskdescription,related_name="description", on_delete=models.CASCADE)
    Detail = models.ForeignKey(lsttaskdetail,related_name="detail", on_delete=models.CASCADE)
    Resource = models.ForeignKey(Person,related_name="Resource", on_delete=models.CASCADE)
    Rate = models.DecimalField(max_digits=4, decimal_places=2)
    RateUnits = models.ForeignKey(lstunit,related_name="rateunits", on_delete=models.CASCADE)
    EstHours = models.DecimalField(max_digits=4, decimal_places=2)
    ActHours = models.DecimalField(max_digits=4,decimal_places=2)
    Comments = models.CharField(max_length=255)
    permission = models.CharField(max_length=255, default="{}")


class WorkActivity(models.Model):
    Server_id = models.IntegerField()
    ParentTask = models.IntegerField()



class lstcountry(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)


class lstcity(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)


class lstaogtype(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)


class btareaofgovernance(models.Model):
    Server_id = models.IntegerField()
    Title = models.CharField(max_length=255)
    AttributeCount = models.IntegerField()


class lstmunicipalitytype(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)


class lstmunicipality(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)


class lstcontacttype(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)


class lstnameprefix(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)


class lstnamesuffix(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)


class lstprofession(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)


class lstprofessiondesignation(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)


class lstprofessionlevel(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)