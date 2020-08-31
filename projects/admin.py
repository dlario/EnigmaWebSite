# Register your models here.
from django.contrib import admin
from .models import Project, ProjectDocument, ProjectMilestone, ProjectRoles, ProjectDocumentGroup, ProjectTask


admin.site.register(ProjectMilestone)

admin.site.register(ProjectRoles)

admin.site.register(ProjectDocumentGroup)

admin.site.register(ProjectTask)

class ProjectDocumentInline(admin.TabularInline):
    model = ProjectDocument
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectDocumentInline]
admin.site.register(Project, ProjectAdmin)
