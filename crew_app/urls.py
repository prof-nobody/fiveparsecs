from django.urls import path
from .views import *

app_name = 'crew_app'
urlpatterns = [
    # path('', crew_roster, name='index'),
    path('', HomePageView.as_view(), name='5p_home'),
    path('create_gear/pd/add/', CreateProtectiveDeviceView.as_view(), name='protective'),
    path('crew/gear/pd/', EquipmentView.as_view(), name='EquipmentView'),
    path('crew/gear/update_gear/<int:pk>', UpdateProtectiveDeviceView.as_view(), name='update_gear'),
    path('fpfh/crew/create', CreateCrewmateView.as_view(), name='crew_create'),
    path('fpfh/crew/update/<int:pk>', UpdateCrewmateView.as_view(), name='crew_update'),
    path('fpfh/crew/list/', CrewView.as_view(), name='crew_list'),
    path('config/species/', SpeciesListView.as_view(), name='species_list'),
    path('config/species/create/', CreateSpeciesView.as_view(), name='species_create'),
    path('config/species/update/<int:pk>', UpdateSpeciesView.as_view(), name='species_update'),
    path('config/background/update/<int:pk>', UpdateBackgroundView.as_view(), name='background_update'),
    path('config/background/', BackgroundView.as_view(), name='background_list'),
    path('config/background/create/', CreateBackgroundView.as_view(), name='background_create'),
    path('config/motivation/update/<int:pk>', UpdateBackgroundView.as_view(), name='motivation_update'),
    path('config/motivation/', BackgroundView.as_view(), name='motivation_list'),
    path('config/motivation/create/', CreateBackgroundView.as_view(), name='motivation_create'),
    path('config/class/update/<int:pk>', UpdateClassView.as_view(), name='class_update'),
    path('config/class/', ClassView.as_view(), name='class_list'),
    path('config/class/create/', CreateClassView.as_view(), name='class_create'),
]
