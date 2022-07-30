from django.contrib import admin
from .models.models import CrewRoster, Campaign, Crewmate, Ship, Equipment, EquipmentTrait, ProtectiveDevice
# Register your models here.


class EquipmentTraitAdmin(admin.ModelAdmin):
    list_display = ('name', 'stat', 'effect')


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class ProtectiveDeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class ShipAdmin(admin.ModelAdmin):
    list_display = ('name', 'type',)


class CrewAdmin(admin.ModelAdmin):
    list_display = ('crew_name', )


class CrewMateAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'leader',)


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('campaign_owner', 'crew_size', 'difficulty',)


admin.site.register(CrewRoster, CrewAdmin)
admin.site.register(Crewmate, CrewMateAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Ship, ShipAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(ProtectiveDevice, ProtectiveDeviceAdmin)
admin.site.register(EquipmentTrait, EquipmentTraitAdmin)
