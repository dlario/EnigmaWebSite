from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('companydetails', views.companydetails, name='companydetails'),
    path('<int:pk>/<slug:companyname>', views.companydetails, name='companydetails'),
    path('userdetails', views.personview.as_view(), name='userdetails'),
    path('companyhome/', views.companyhome, name='companyhome'),
    path('companyhome2/<int:company_id>/', views.companyhome2, name='companyhome2'),
    path('person/', views.PersonCRUDViewSet.list(), name='person'),
    path('person/new/', views.PersonCRUDViewSet.create(), name='new-person'),
    path('person/<int:pk>/edit/', views.PersonCRUDViewSet.update(), name='edit-person'),
    path('person/<int:pk>/delete/', views.PersonCRUDViewSet.delete(), name='delete-person'),
    path('person/<int:pk>/delete2/', views.person_delete, name='person_delete'),
    path('person/<int:pk>/update/', views.person_update, name='person_update'),
    path('person/create/', views.person_create, name='person_create'),
    path('personlist', views.person_list, name='person_list'),
    path('company/', views.CompanyCRUDViewSet.list(), name='company'),
    path('company/new/', views.CompanyCRUDViewSet.create(), name='new-company'),
    path('company/<int:pk>/edit/', views.CompanyCRUDViewSet.update(), name='edit-company'),
    path('company/<int:pk>/delete/', views.CompanyCRUDViewSet.delete(), name='delete-company'),
]