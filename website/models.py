from django.db import models

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