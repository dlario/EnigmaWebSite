from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('bookinspection', views.BookView.as_view(), name='bookinspection'),
    path('create', views.create, name='create'),
    path('inspections', views.inspections, name='inspections'),
    path('inspectionlisttable', views.InspectionListView.as_view(), name='inspectionlisttable'),
    path('inspectiontable', views.FooTableView.as_view(), name='inspectionlisttable'),
    path('<int:pk>/images', views.inspectionimages, name='inspectionimages'),
    path('<int:pk>/documents', views.inspectiondocuments, name='inspectiondocuments'),
]
