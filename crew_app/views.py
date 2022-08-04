from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.urls import reverse_lazy
from django.utils.text import slugify
from .models.models import *
from .models.update import Update
from .serializers import *
from django.shortcuts import get_object_or_404
# Create your views here.


class CrewRosterView(generic.ListView):
    pass


class RosterDetailView(generic.DetailView):
    pass


class CreateRosterView(CreateView):
    pass


class UpdateRosterView(UpdateView):
    pass


class ListShipView(generic.ListView):
    context_object_name = "ships"
    template_name = "crew/shipView.html"
    model = Ship

    def get_queryset(self):
        return Ship.objects.order_by('pk')


class ShipDetailView(generic.DetailView):
    context_object_name = "ship"


class CreateShipView(CreateView):
    model = Ship
    fields = ['hull', 'name', 'debt']
    template_name = 'crew/ship.html'
    success_url = reverse_lazy('crew_app:ship_list')

    def form_valid(self, form):
        hul = form.instance.hull
        hp = get_object_or_404(ShipHull, pk=hul.pk)
        form.instance.hull_points_max = hp.hull_points
        form.instance.hull_points_cur = hp.hull_points
        form.instance.upgrades = ['none']
        return super().form_valid(form)


class UpdateShipView(UpdateView):
    model = Ship
    fields = ['hull', 'name', 'debt']
    template_name = 'crew/ship.html'
    success_url = reverse_lazy('crew_app:ship_list')


class ListConfigShipView(generic.ListView):

    template_name = 'crew/shipConfigView.html'
    model = ShipHull
    context_object_name = 'shiphull_list'

    def get_queryset(self):
        return ShipHull.objects.order_by('type')


class CreateConfigShipView(CreateView):
    template_name = 'crew/shipConfig.html'
    model = ShipHull
    fields = ['roll', 'hull', 'traits', 'hull_points', 'debt']
    success_url = reverse_lazy('crew_app:shipconfig_list')


class UpdateConfigShipView(UpdateView):
    template_name = 'crew/shipConfig.html'
    model = ShipHull
    fields = ['roll', 'hull', 'traits', 'hull_points', 'debt']
    success_url = reverse_lazy('crew_app:shipconfig_list')


class ListConfigShipComponentView(generic.ListView):
    template_name = 'crew/shipComponentView.html'
    model = ShipComponent
    context_object_name = 'shipcomponent_list'

    def get_queryset(self):
        return ShipComponent.objects.order_by('name')


class CreateConfigShipComponentView(CreateView):
    template_name = 'crew/shipConfig.html'
    model = ShipComponent
    fields = ['name', 'cost', 'description']
    success_url = reverse_lazy('crew_app:shipcomponent_list')


class UpdateConfigShipComponentView(UpdateView):
    template_name = 'crew/shipConfig.html'
    model = ShipComponent
    fields = ['name', 'cost', 'description']
    success_url = reverse_lazy('crew_app:shipcomponent_list')


class HomePageView(generic.ListView):
    template_name = 'crew/fiveparsecs.html'
    model = Update
    context_object_name = 'updates'

    def get_queryset(self):
        return Update.objects.order_by('-created_on')[:3]


class CreateUpdatesView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('is_staff', )
    template_name = 'crew/updates.html'
    model = Update
    fields = ['title', 'content', ]
    success_url = reverse_lazy('5p_home')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateUpdatesView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('is_staff',)
    template_name = 'crew/updates.html'
    model = Update
    fields = ['title', 'content', ]
    success_url = reverse_lazy('5p_home')


class DetailUpdatesView(generic.DetailView):
    template_name = 'crew/fiveparsecs_details.html'
    model = Update
    context_object_name = 'update'


class SpeciesListView(generic.ListView):
    template_name = 'crew/speciesView.html'
    model = Species
    context_object_name = 'species_list'

    def get_queryset(self):
        return Species.objects.order_by('species')


class CreateSpeciesView(CreateView):
    template_name = 'crew/species.html'
    model = Species
    fields = ['species', 'reactions', 'speed', 'combat_skill', 'toughness', 'savvy']
    success_url = reverse_lazy('species_list')


class UpdateSpeciesView(UpdateView):
    template_name = 'crew/species.html'
    model = Species
    fields = ['species', 'reactions', 'speed', 'combat_skill', 'toughness', 'savvy']
    success_url = reverse_lazy('species_list')


class EquipmentView(generic.ListView):
    template_name = 'crew/gearView.html'
    model = ProtectiveDevice

    fields = ['id', 'name', 'category', 'description', 'trait', ]
    context_object_name = 'gear_list'

    def get_queryset(self):
        return ProtectiveDevice.objects.order_by('name')


class CreateProtectiveDeviceView(CreateView):
    template_name = 'crew/equipment.html'
    model = ProtectiveDevice
    fields = ['name', 'category', 'description', 'trait', ]
    success_url = reverse_lazy('gear')


class UpdateProtectiveDeviceView(UpdateView):
    template_name = 'crew/equipment.html'
    model = ProtectiveDevice
    fields = ['name', 'category', 'description', 'trait', ]
    success_url = reverse_lazy('gear')


class CreateBackgroundView(CreateView):
    template_name = 'crew/background.html'
    model = Background
    fields = ['name', 'effect', 'resources', 'starting_rolls', 'roll' ]
    success_url = reverse_lazy('background_list')


class UpdateBackgroundView(UpdateView):
    template_name = 'crew/background.html'
    model = Background
    fields = ['name', 'effect', 'resources', 'starting_rolls', 'roll' ]
    success_url = reverse_lazy('background_list')


class BackgroundView(generic.ListView):
    template_name = 'crew/backgroundView.html'
    model = Background

    context_object_name = 'background_list'

    def get_queryset(self):
        return Background.objects.order_by('roll')


class CreateMotivationView(CreateView):
    template_name = 'crew/background.html'
    model = Motivation
    fields = ['name', 'effect', 'resources', 'starting_rolls', 'roll' ]
    success_url = reverse_lazy('motivation_list')


class UpdateMotivationView(UpdateView):
    template_name = 'crew/background.html'
    model = Motivation
    fields = ['name', 'effect', 'resources', 'starting_rolls', 'roll' ]
    success_url = reverse_lazy('motivation_list')


class MotivationView(generic.ListView):
    template_name = 'crew/motivationView.html'
    model = Motivation

    context_object_name = 'motivation_list'

    def get_queryset(self):
        return Motivation.objects.order_by('roll')


class CreateClassView(CreateView):
    template_name = 'crew/background.html'
    model = Class
    fields = ['name', 'effect', 'resources', 'starting_rolls', 'roll' ]
    success_url = reverse_lazy('class_list')


class UpdateClassView(UpdateView):
    template_name = 'crew/background.html'
    model = Class
    fields = ['name', 'effect', 'resources', 'starting_rolls', 'roll' ]
    success_url = reverse_lazy('class_list')


class ClassView(generic.ListView):
    template_name = 'crew/classView.html'
    model = Class

    context_object_name = 'class_list'

    def get_queryset(self):
        return Class.objects.order_by('roll')


class CrewView(generic.ListView):
    template_name = 'crew/crewView.html'
    model = Crewmate

    fields = ['name', 'experience_points', 'crew_class', 'owner', ]
    context_object_name = 'crewmates'

    def get_queryset(self):
        return Crewmate.objects.order_by('name')


class CreateCrewmateView(CreateView):
    template_name = 'crew/equipment.html'
    model = Crewmate
    fields = ['name', 'species', 'background', 'motivation', 'crew_class', 'leader', ]
    success_url = reverse_lazy('crew_app:crew_list')


class UpdateCrewmateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'crew/equipment.html'
    model = Crewmate
    fields = ['name', 'species', 'background', 'motivation', 'crew_class', 'leader', ]
    success_url = reverse_lazy('crew_app:crew_list')

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


@api_view(['GET', 'POST'])
def crew_roster(request):
    if request.method == 'GET':
        data = CrewRoster.objects.all()

        serializer = CrewRosterSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CrewRosterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def crew_roster_details(request, pk):
    try:
        crew = CrewRoster.objects.get(pk=pk)
    except CrewRoster.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CrewRosterSerializer(crew, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        crew.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
