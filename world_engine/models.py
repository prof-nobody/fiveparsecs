from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin

# Create your models here.


class WorldTrait(models.Model):
    trait_die_min = models.CharField(max_length=4, default=0)
    trait_die_max = models.CharField(max_length=4, default=0)
    trait_name = models.CharField(max_length=200)
    trait_description = models.TextField()
    trait_variables = models.CharField(max_length=200, null=True)
    trait_ai_description = models.CharField(max_length=200, null=True)
    traits_conflicting = models.CharField(max_length=200, null=True)
    traits_complementing = models.CharField(max_length=200, null=True)


class WorldDetail(models.Model):
    PREHISTORY = "PH"
    CLASSICAL = 'CL'
    PRE_INDUSTRIAL = 'PI'
    INDUSTRIAL_REVOLUTION = 'IR'
    EARLY_COMPUTER = 'EC'
    COMPUTER = 'CP'
    SPACEFARING = 'SF'
    NULL = 'NL'
    NATIVE_SENTIENT_ERA = [
        (PREHISTORY, "Pre-History"),
        (CLASSICAL, 'Classical'),
        (PRE_INDUSTRIAL, 'Pre-Industrial'),
        (INDUSTRIAL_REVOLUTION, 'Industrial Revolution'),
        (EARLY_COMPUTER, 'Early Computer Age'),
        (COMPUTER, 'Computer Age'),
        (SPACEFARING, 'Spacefaring'),
        (NULL, 'No sentient life'),
    ]
    world_name = models.CharField(max_length=100)
    world_description = models.TextField()
    wild_galaxy = models.BooleanField(default=True)
    auto_roll = models.BooleanField(default=True)
    world_trait_one = models.CharField(max_length=100)
    world_trait_two = models.CharField(max_length=100)
    native_sentient = models.BooleanField(default=True)
    native_sentient_era = models.CharField(
        max_length=2,
        choices=NATIVE_SENTIENT_ERA,
        default=NULL
    )
    colonized = models.BooleanField(default=False)



