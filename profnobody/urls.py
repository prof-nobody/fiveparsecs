"""profnobody URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from crew_app.views import *
from rest_framework import routers

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('worldengine/', include('world_engine.urls')),

    # re_path(r'^api/crewroster/$', views.crew_roster),
    # re_path(r'^api/crewroster/([0-9])$', views.crew_roster_details),
    path('accounts/', include('django.contrib.auth.urls')),
    path('fpfh/', HomePageView.as_view(), name='5p_home'),
    path('fpfh/config/background/update/<int:pk>', UpdateBackgroundView.as_view(), name='background_update'),
    path('fpfh/config/background/', BackgroundView.as_view(), name='background_list'),
    path('fpfh/config/background/create/', CreateBackgroundView.as_view(), name='background_create'),
    path('fpfh/crew/create_gear/', CreateProtectiveDeviceView.as_view(), name='protective'),
    path('fpfh/crew/gear/pd/', EquipmentView.as_view(), name='gear'),
    path('fpfh/crew/create', CreateCrewmateView.as_view(), name='crew_create'),
    path('fpfh/crew/update/<int:pk>', UpdateCrewmateView.as_view(), name='crew_update'),
    path('fpfh/crew/list/', CrewView.as_view(), name='crew_list'),
    path('fpfh/crew/gear/update_gear/<int:pk>', UpdateProtectiveDeviceView.as_view(), name='update_gear'),
    path('fpfh/config/species/', SpeciesListView.as_view(), name='species_list'),
    path('fpfh/config/species/create/', CreateSpeciesView.as_view(), name='species_create'),
    path('fpfh/config/species/update/<int:pk>', UpdateSpeciesView.as_view(), name='species_update'),
    path('fpfh/config/motivation/update/<int:pk>', UpdateMotivationView.as_view(), name='motivation_update'),
    path('fpfh/config/motivation/', MotivationView.as_view(), name='motivation_list'),
    path('fpfh/config/motivation/create/', CreateMotivationView.as_view(), name='motivation_create'),
    path('fpfh/config/class/update/<int:pk>', UpdateClassView.as_view(), name='class_update'),
    path('fpfh/config/class/', ClassView.as_view(), name='class_list'),
    path('fpfh/config/class/create/', CreateClassView.as_view(), name='class_create'),
    path('', include('blog.urls')),
]
