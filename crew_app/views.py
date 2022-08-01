from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.urls import reverse_lazy
from django.utils.text import slugify
from .models.models import *
from .models.update import Update
from .serializers import *
# Create your views here.


class HomePageView(generic.ListView):
    template_name = 'crew/fiveparsecs.html'
    model = Update
    context_object_name = 'updates'

    def get_queryset(self):
        return Update.objects.order_by('-created_on')[:3]


class CreateUpdatesView(LoginRequiredMixin, CreateView):
    template_name = 'crew/updates.html'
    model = Update
    fields = ['title', 'content', ]
    success_url = reverse_lazy('5p_home')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateUpdatesView(LoginRequiredMixin, UpdateView):
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

    fields = ['name', 'experience_points', 'crew_class', ]
    context_object_name = 'crewmates'

    def get_queryset(self):
        return Crewmate.objects.order_by('name')


class CreateCrewmateView(CreateView):
    template_name = 'crew/equipment.html'
    model = Crewmate
    fields = ['name', 'species', 'background', 'motivation', 'crew_class', 'leader', ]
    success_url = reverse_lazy('crew_list')


class UpdateCrewmateView(UpdateView):
    template_name = 'crew/equipment.html'
    model = Crewmate
    fields = ['name', 'species', 'background', 'motivation', 'crew_class', 'leader', ]
    success_url = reverse_lazy('crew_list')


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
