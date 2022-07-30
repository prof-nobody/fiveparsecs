from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.postgres.fields import ArrayField, IntegerRangeField


class EquipmentTrait(models.Model):
    MOD = (
        ('+', "Positive"),
        ('-', 'Negative'),
        ('*', 'Multiply'),
        ('0', 'None'),
    )
    CATEGORY = (
        ('CN', 'Consumable'),
        ('PR', 'Protective Device'),
        ('IM', 'Implant'),
        ('UD', 'Utility Device'),
        ('OI', 'On-board Items'),
        ('GM', 'Gun Mod'),
        ('GS', 'Gun Sight'),
        ('WP', 'Weapon'),
        ('GN', 'Generic'),
    )

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=300, choices=CATEGORY, default='CN')
    stat = models.CharField(max_length=100)
    modifier = models.CharField(max_length=1, choices=MOD)
    effect = models.IntegerField()

    def __str__(self):
        return self.name


class GunMod(models.Model):
    MOD = (
        ('+', "Positive"),
        ('-', 'Negative'),
        ('*', 'Multiply'),
        ('0', 'None'),
    )

    name = models.CharField(max_length=200)
    desc = models.TextField()
    stat = models.CharField(max_length=100)
    modifier = models.CharField(max_length=1, choices=MOD)
    effect = models.IntegerField()
    restriction = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class GunSight(models.Model):
    MOD = (
        ('+', "Positive"),
        ('-', 'Negative'),
        ('*', 'Multiply'),
        ('0', 'None'),
    )

    name = models.CharField(max_length=200)
    desc = models.TextField()
    stat = models.CharField(max_length=100)
    modifier = models.CharField(max_length=1, choices=MOD)
    effect = models.IntegerField()
    restriction = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    CATEGORY = (
        ('CN', 'Consumable'),
        ('PR', 'Protective Device'),
        ('IM', 'Implant'),
        ('UD', 'Utility Device'),
        ('OI', 'On-board Items'),
        ('GM', 'Gun Mod'),
        ('GS', 'Gun Sight'),
        ('WP', 'Weapon'),
    )
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CATEGORY, default=None)
    equippable = models.BooleanField()
    stackable = models.BooleanField()
    description = models.CharField(max_length=600, null=True)
    trait = models.ManyToManyField(EquipmentTrait, blank=True)
    range = models.IntegerField(blank=True)
    shots = models.IntegerField(blank=True)
    dmg = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


class ProtectiveDevice(models.Model):

    CATEGORY = (
        ('SC', 'Screen'),
        ('AR', 'Armor'),
    )
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CATEGORY, default=None)
    equippable = models.BooleanField(default=True)
    description = models.CharField(max_length=600, null=True)
    trait = models.ManyToManyField(EquipmentTrait, blank=True, )

    def __str__(self):
        return self.name


class ProtectiveDeviceForm(ModelForm):
    class Meta:
        model = ProtectiveDevice
        fields = ['name', 'category', 'description', 'trait', ]


class Item(models.Model):
    CATEGORY = (
        ('IM', 'Implant'),
        ('UD', 'Utility Device'),
        ('OI', 'On-board Items'),
    )
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CATEGORY, default=None)
    equippable = models.BooleanField(default=False)
    description = models.CharField(max_length=600, null=True)
    trait = models.ManyToManyField(EquipmentTrait, blank=True, )

    def __str__(self):
        return self.name


class Consumable(models.Model):

    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    equippable = models.BooleanField(default=False)
    description = models.CharField(max_length=600, null=True)
    trait = models.ManyToManyField(EquipmentTrait, blank=True, )

    def __str__(self):
        return self.name


class Weapon(models.Model):
    CLASS = (
        ('PS', 'Pistol'),
        ('ML', 'Melee'),
        ('RF', 'Rifle'),
        ('OT', 'Other'),
    )
    name = models.CharField(max_length=200)
    equippable = models.BooleanField(default=True)
    description = models.CharField(max_length=600, null=True)
    trait = models.ManyToManyField(EquipmentTrait, blank=True,)
    mod = models.ManyToManyField(GunMod, blank=True, )
    range = models.IntegerField(blank=True)
    shots = models.IntegerField(blank=True)
    dmg = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


class CrewStash(models.Model):
    pass


class Ship(models.Model):
    SHIP_TYPE = (
        ('WF', 'Worn Freighter'),
        ('RTT', 'Retired Troop Transport'),
        ('SAV', 'Strange Alien Vessel'),
        ('UPS', 'Upgraded Shuttle'),
        ('RSS', 'Retired Scout Ship'),
        ('RSV', 'Repurposed Science Vessel'),
        ('BMV', 'Battered Mining Ship'),
        ('UMC', 'Unreliable Merchant Cruiser'),
        ('FDV', 'Former Diplomatic Vessel'),
        ('ALC', 'Ancient Low-Tech Craft'),
        ('BSW', 'Built from Salvaged Wrecks'),
        ('RMS', 'Retired Military Patrol Ship'),
    )

    name = models.CharField(max_length=300,)
    type = models.CharField(max_length=200, choices=SHIP_TYPE)
    debt = models.CharField(max_length=4,)
    hull_points_max = models.CharField(max_length=5,)
    hull_points_cur = models.CharField(max_length=5,)
    traits = models.CharField(max_length=500, blank=True,)
    upgrades = models.CharField(max_length=500, blank=True,)

    def __str__(self):
        return self.name


class Species(models.Model):
    SPECIES = (
        ('BH', 'Baseline Human'),
        ('BT', 'Bot'),
        ('EN', 'Engineer'),
        ("KE", "K'Erin"),
        ("SL", "Soulless"),
        ("PC", "Precursor"),
        ("FL", "Feral"),
        ("SW", "Swift"),
        ("DC", "De-Converted"),
        ("UA", "Unity Agent"),
        ("MP", "Mysterious Past"),
        ("HA", "Hakshan"),
        ("ST", "Stalker"),
        ("HU", "Hulker"),
        ("HR", "Hopeful Rookie"),
        ("GU", "Genetic Uplift"),
        ("MU", "Mutant"),
        ("AB", "Assault Bot"),
        ("MA", "Manipulator"),
        ("PR", "Primitive"),
        ("FE", "Feeler"),
        ("ES", "Emo-Suppressed"),
        ("MI", "Minor Alien"),
        ("TR", "Traveler"),
        ("EM", "Empath"),
        ("BU", "Bio-upgrade"),

    )

    species = models.CharField(
        max_length=200,
        choices=SPECIES,
        default='BH',
    )
    reactions = models.CharField(max_length=30)
    speed = models.CharField(max_length=30)
    combat_skill = models.CharField(max_length=30)
    toughness = models.CharField(max_length=30)
    savvy = models.CharField(max_length=30)


class Background(models.Model):
    name = models.CharField(max_length=300)
    effect = ArrayField(models.CharField(max_length=300), blank=True)
    resources = ArrayField(models.CharField(max_length=300), blank=True)
    starting_rolls = ArrayField(models.CharField(max_length=300), blank=True)
    roll = IntegerRangeField(default=0)


class Motivation(models.Model):
    roll = IntegerRangeField(default=0)
    name = models.CharField(max_length=300)
    effect = ArrayField(models.CharField(max_length=300), blank=True)
    resources = ArrayField(models.CharField(max_length=300), blank=True)
    starting_rolls = ArrayField(models.CharField(max_length=300), blank=True)


class Class(models.Model):
    roll = IntegerRangeField(default=0)
    name = models.CharField(max_length=300)
    effect = ArrayField(models.CharField(max_length=300), blank=True)
    resources = ArrayField(models.CharField(max_length=300), blank=True)
    starting_rolls = ArrayField(models.CharField(max_length=300), blank=True)


class Crewmate(models.Model):

    # crew_roster = models.ForeignKey(CrewRoster, on_delete=models.CASCADE, )
    name = models.CharField(max_length=200)
    species = models.ForeignKey(
        Species,
        on_delete=models.CASCADE,
    )
    luck_points = models.CharField(max_length=30, blank=True,)
    equipment = models.CharField(max_length=400, blank=True,)
    experience_points = models.CharField(max_length=30, default=0)
    background = models.CharField(max_length=200, blank=True,)
    motivation = models.CharField(max_length=200, blank=True,)
    crew_class = models.CharField(max_length=200, blank=True,)
    leader = models.BooleanField(default=False)
    notes = models.CharField(max_length=500, blank=True, )
    weaponA = models.CharField(max_length=100, blank=True)
    weaponB = models.CharField(max_length=100, blank=True)
    pistol = models.CharField(max_length=100, blank=True)
    blade = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    CREW_SIZE = (
        ('6', "Crew Size 6"),
        ('5', "Crew Size 5"),
        ('4', "Crew Size 4"),
    )

    VICTORY_CONDITION = (
        ('P20', 'Play 20 campaign turns'),
        ('P50', 'Play 50 campaign turns'),
        ('P10', 'Play 100 campaign turns'),
        ('C3Q', 'Complete 3 Quests'),
        ('C5Q', 'Complete 5 Quests'),
        ('C1Q', 'Complete 10 Quests'),
        ('W20', 'Win 20 tabletop battles'),
        ('W50', 'Win 50 tabletop battles'),
        ('W10', 'Win 100 tabletop battles'),
        ('K10', 'Kill 10 Unique Individuals'),
        ('K25', 'Kill 25 Unique Individuals'),
        ('UP1', 'Upgrade a single character 10 times'),
        ('UP3', 'Upgrade 3 characters 10 times'),
        ('UP5', 'Upgrade 5 characters 10 times'),
        ('PC5', 'Play 50 campaign turns in Challenging mode'),
        ('PH5', 'Play 50 campaign turns in Hardcore mode'),
        ('PI5', 'Play 50 campaign turns in Insanity mode'),
    )

    DIFFICULTY = (
        ('EZ', 'Easy'),
        ('NM', 'Normal'),
        ('CH', 'Challenging'),
        ('HC', 'Hardcore'),
        ('IN', 'Insanity'),
    )

    campaign_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    crew_size = models.CharField(
        max_length=1,
        choices=CREW_SIZE,
        default=None,
    )
    victory_condition = models.CharField(
        max_length=3,
        choices=VICTORY_CONDITION,
    )
    difficulty = models.CharField(
        max_length=2,
        choices=DIFFICULTY,
    )
    name = models.CharField(max_length=400)
    house_rules = models.CharField(max_length=400)
    campaign_turn = models.CharField(max_length=4)
    story_points = models.CharField(max_length=3)
    worlds_visited = models.CharField(max_length=500)
    current_world = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CrewRoster(models.Model):
    MET = (
        ("Hired", "Hired by a random member of the group"),
        ("Pursuit", "Pursuit of random group member's motivation"),
        ("Trouble", "Being in trouble with the authorities"),
        ("Enemy", "A common enemy"),
        ("Cause", "A common cause or belief"),
        ("Meeting", "A random meeting in a bar"),
        ("PrevJob", "A previous job"),
        ("Mutual", "Mutual protection is a hostile universe"),
        ("WarBuds", "Being old war buddies"),
    )
    CHARACTERIZED = (
        ('Rogues', 'Lovable Rogues'),
        ('Professionals', 'Consummate professionals'),
        ('Outlaws', 'Cut-throat Outlaws'),
        ('Defenders', 'Defenders of the down-trodden'),
        ('Rebels', 'Hardened rebels'),
        ('Scum', 'Starport scum'),
        ('Bandits', 'Somewhat honorable bandits'),
        ('Credits', 'In it for the credits'),
        ('Dream', 'Living the dream!'),
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    crew_name = models.CharField(max_length=200)
    crew_origin_met = models.CharField(max_length=300)
    crew_origin_description = models.CharField(max_length=300)
    crew_mates = models.ManyToManyField(Crewmate)
    current_campaign = models.ForeignKey(Campaign, on_delete=models.PROTECT)
    prev_campaigns = models.CharField(max_length=300)
    ship_type = models.ForeignKey(
        Ship,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f"{self.crew_name}"
