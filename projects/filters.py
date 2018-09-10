from .models import Project
from django_filters import FilterSet, NumberFilter, CharFilter


class ProjectFilter(FilterSet):

    class Meta:
        model = Project
        #fields = ['project_number', 'owner']
        fields = {
            'project_number': ['contains'],
            'client': ['exact'],
            'title': ['contains'],
        }

class InspectionTitleFilter(FilterSet):
    class Meta:
        model = Project
        # fields = ['project_number', 'owner']
        fields = {
            'project_number': ['contains'],
            'title': ['contains'],
        }