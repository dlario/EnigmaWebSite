from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('project/', views.ProjectCRUDViewSet.list(), name='project'),
    path('project/new/', views.ProjectCRUDViewSet.create(), name='new-project'),
    path('project/<int:pk>/edit/', views.ProjectCRUDViewSet.update(), name='edit-project'),
    path('project/<int:pk>/delete/', views.ProjectCRUDViewSet.delete(), name='delete-project'),
]