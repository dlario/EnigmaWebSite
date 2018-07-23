from django.urls import path, include
from . import views

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('team', views.team, name='team'),
]