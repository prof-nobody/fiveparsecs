from django.contrib import admin
from .models import WorldTrait, WorldDetail

# Register your models here.


class WorldTraitModel(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['trait_name', 'trait_description', 'trait_variables',
                           'trait_ai_description', 'trait_die_min', 'trait_die_max', ]})
    ]
    list_display = ('trait_name', 'trait_die_min', 'trait_die_max', )


class WorldDetailModel(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['world_name', 'world_description', 'native_sentient', 'native_sentient_era', 'colonized', ]}),
        ('World Traits', {'fields': ['world_trait_one', 'world_trait_two', 'wild_galaxy', ]})
    ]
    list_display = ('world_name', 'world_trait_one', 'world_trait_two',)


    # inlines = ['trait_die_min', 'trait_die_max', ]


admin.site.register(WorldTrait, WorldTraitModel)
admin.site.register(WorldDetail, WorldDetailModel)
