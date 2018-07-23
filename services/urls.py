from django.contrib import admin
from django.urls import path, include
from services import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('engineering', views.engineering, name='engineering'),
    path('equipmentinspection', views.equipmentinspection, name='equipmentinspection'),
    path('fabrication', views.fabrication, name='fabrication'),
    path('testing', views.testing, name='testing'),
    path('toolinspection', views.toolinspection, name='toolinspection'),
]
