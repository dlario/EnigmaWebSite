from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('clientdetails', views.clientdetails, name='clientdetails'),
    path('userdetails', views.personview.as_view(), name='userdetails'),
    path('clienthome', views.clienthome, name='clienthome'),
]