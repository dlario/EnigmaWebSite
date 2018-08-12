from django.urls import path, include
from . import views
from django.conf import settings
from django.views import defaults as default_views

urlpatterns = [
    path('detail', views.detail, name='detail'),
    path('home', views.home, name='home'),
    path('index', views.index, name='index'),
    path('<int:inspection_id>', views.detail, name='detail'),
    path('createproject', views.MainView.as_view(), name='createproject'),
    path('create', views.create, name='create'),
    path('inspections', views.inspections, name='inspections'),
    path('inspectionlisttable', views.InspectionListView.as_view(), name='inspectionlisttable'),
    path('inspectiontable', views.FooTableView.as_view(), name='inspectionlisttable'),
]