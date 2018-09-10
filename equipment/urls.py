from django.urls import path, include
from . import views
from django.conf import settings
from django.views import defaults as default_views

urlpatterns = [
    path('equipment/detail/<int:pk>', views.equipmentdetail, name='equipmentdetail'),
    path('equipmentlist', views.equipmentlist, name='equipmentlist'),
]
