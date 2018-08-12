from django.contrib import admin

# Register your models here.
from .models import Inspection, InspectionImage, InspectionDocument

class InspectionDocumentInline(admin.TabularInline):
    model = InspectionDocument
    extra = 3

class InspectionAdmin(admin.ModelAdmin):
    inlines = [InspectionDocumentInline]

admin.site.register(Inspection, InspectionAdmin)
