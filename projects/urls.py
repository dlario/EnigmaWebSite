from django.urls import path, include
from . import views

urlpatterns = [
    path('bookinspection', views.BookView.as_view(), name='bookinspection'),
    path('<int:project_id>/<slug:project_number>', views.detail, name='detail'),
    path('', views.uploadfiles, name='uploadfiles'),
    path('project/create', views.create, name='create'),
    path('projects', views.projects, name='projects'),
    path('project/', views.ProjectCRUDViewSet.list(), name='project'),
    path('project/new/', views.ProjectCRUDViewSet.create(), name='new-project'),
    path('project/<int:pk>/edit/', views.ProjectCRUDViewSet.update(), name='edit-project'),
    path('project/<int:pk>/delete/', views.ProjectCRUDViewSet.delete(), name='delete-project'),
    path('project/<int:pk>/documents', views.inspectiondocuments, name='inspectiondocuments'),
    path('projecttable', views.FooTableView.as_view(), name='projecttable'),
    path('projectlisttable', views.ProjectListView.as_view(), name='projectlist'),
    path('projecttable2', views.ProjectTableView.as_view(), name='projecttable2'),
    path('project/<int:projectpk>/roles/<int:rolepk>', views.ProjectRoleCrudViewset.list(), name='projectrole'),
    path('project/<int:projectpk>/roles/new/', views.ProjectRoleCrudViewset.create(), name='new-projectrole'),
    path('project/<int:projectpk>/roles/<int:rolepk>/edit/', views.ProjectRoleCrudViewset.update(), name='edit-projectrole'),
    path('project/<int:projectpk>/roles/<int:rolepk>/delete/', views.ProjectRoleCrudViewset.delete(), name='delete-projectrole'),
    path('django_popup_view_field/', include('django_popup_view_field.urls', namespace="django_popup_view_field")),
]
