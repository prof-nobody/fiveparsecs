from django.urls import path
from .views import *

app_name = 'crew_app'
urlpatterns = [
    # path('', crew_roster, name='index'),
    path('', HomePageView.as_view(), name='5p_home'),
    path('config/updates/create/', CreateUpdatesView.as_view(), name='updates_create'),
    path('config/updates/update/<int:pk>', UpdateUpdatesView.as_view(), name='updates_update'),
    path('config/ship/create/', CreateConfigShipView.as_view(), name='shipconfig_create'),
    path('config/ship/update/<int:pk>', UpdateConfigShipView.as_view(), name='shipconfig_update'),
    path('config/ship/list/', ListConfigShipView.as_view(), name='shipconfig_list'),

    path('config/ship/component/create/', CreateConfigShipComponentView.as_view(), name='shipcomponent_create'),
    path('config/ship/component/update/<int:pk>', UpdateConfigShipComponentView.as_view(), name='shipcomponent_update'),
    path('config/ship/component/list/', ListConfigShipComponentView.as_view(), name='shipcomponent_list'),
    path('updates/<slug:slug>', DetailUpdatesView.as_view(), name='updates_detail'),
    path('create_gear/pd/add/', CreateProtectiveDeviceView.as_view(), name='protective'),
    path('crew/gear/pd/', EquipmentView.as_view(), name='EquipmentView'),
    path('crew/gear/update_gear/<int:pk>', UpdateProtectiveDeviceView.as_view(), name='update_gear'),
    path('crew/create', CreateCrewmateView.as_view(), name='crew_create'),
    path('crew/update/<int:pk>', UpdateCrewmateView.as_view(), name='crew_update'),
    path('crew/list/', CrewView.as_view(), name='crew_list'),
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
    path('crew/ship/create/', CreateShipView.as_view(), name='ship_create'),
    path('crew/ship/update/<int:pk>', UpdateShipView.as_view(), name='ship_update'),
    path('crew/ship/list/', ListShipView.as_view(), name='ship_list'),
]
