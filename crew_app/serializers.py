from rest_framework import serializers
from .models.models import CrewRoster


class CrewRosterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CrewRoster
        fields = ('pk', 'crew_name', 'crew_origin_met', 'crew_origin_description', )