# Generated by Django 4.0.6 on 2022-07-26 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crew_size', models.CharField(choices=[('6', 'Crew Size 6'), ('5', 'Crew Size 5'), ('4', 'Crew Size 4')], default=None, max_length=1)),
                ('victory_condition', models.CharField(choices=[('P20', 'Play 20 campaign turns'), ('P50', 'Play 50 campaign turns'), ('P10', 'Play 100 campaign turns'), ('C3Q', 'Complete 3 Quests'), ('C5Q', 'Complete 5 Quests'), ('C1Q', 'Complete 10 Quests'), ('W20', 'Win 20 tabletop battles'), ('W50', 'Win 50 tabletop battles'), ('W10', 'Win 100 tabletop battles'), ('K10', 'Kill 10 Unique Individuals'), ('K25', 'Kill 25 Unique Individuals'), ('UP1', 'Upgrade a single character 10 times'), ('UP3', 'Upgrade 3 characters 10 times'), ('UP5', 'Upgrade 5 characters 10 times'), ('PC5', 'Play 50 campaign turns in Challenging mode'), ('PH5', 'Play 50 campaign turns in Hardcore mode'), ('PI5', 'Play 50 campaign turns in Insanity mode')], max_length=3)),
                ('difficulty', models.CharField(choices=[('EZ', 'Easy'), ('NM', 'Normal'), ('CH', 'Challenging'), ('HC', 'Hardcore'), ('IN', 'Insanity')], max_length=2)),
                ('name', models.CharField(max_length=400)),
                ('house_rules', models.CharField(max_length=400)),
                ('campaign_turn', models.CharField(max_length=4)),
                ('story_points', models.CharField(max_length=3)),
                ('worlds_visited', models.CharField(max_length=500)),
                ('current_world', models.CharField(max_length=100)),
                ('campaign_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Crewmate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('species', models.CharField(choices=[('BH', 'Baseline Human'), ('EN', 'Engineer'), ('KE', "K'Erin"), ('SL', 'Soulless'), ('PC', 'Precursor'), ('FL', 'Feral'), ('SW', 'Swift'), ('DC', 'De-Converted'), ('UA', 'Unity Agent'), ('MP', 'Mysterious Past'), ('HA', 'Hakshan'), ('ST', 'Stalker'), ('HU', 'Hulker'), ('HR', 'Hopeful Rookie'), ('GU', 'Genetic Uplift'), ('MU', 'Mutant'), ('AB', 'Assault Bot'), ('MA', 'Manipulator'), ('PR', 'Primitive'), ('FE', 'Feeler'), ('ES', 'Emo-Suppressed'), ('MI', 'Minor Alien'), ('TR', 'Traveler'), ('EM', 'Empath'), ('BU', 'Bio-upgrade')], default='BH', max_length=200)),
                ('reactions', models.CharField(max_length=30)),
                ('speed', models.CharField(max_length=30)),
                ('combat_skill', models.CharField(max_length=30)),
                ('toughness', models.CharField(max_length=30)),
                ('savvy', models.CharField(max_length=30)),
                ('luck_points', models.CharField(blank=True, max_length=30)),
                ('equipment', models.CharField(blank=True, max_length=400)),
                ('experience_points', models.CharField(default=0, max_length=30)),
                ('background', models.CharField(blank=True, max_length=200)),
                ('motivation', models.CharField(blank=True, max_length=200)),
                ('crew_class', models.CharField(blank=True, max_length=200)),
                ('leader', models.BooleanField(default=False)),
                ('notes', models.CharField(blank=True, max_length=500)),
                ('weaponA', models.CharField(blank=True, max_length=100)),
                ('weaponB', models.CharField(blank=True, max_length=100)),
                ('pistol', models.CharField(blank=True, max_length=100)),
                ('blade', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CrewStash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentTrait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('CN', 'Consumable'), ('PR', 'Protective Device'), ('IM', 'Implant'), ('UD', 'Utility Device'), ('OI', 'On-board Items'), ('GM', 'Gun Mod'), ('GS', 'Gun Sight'), ('WP', 'Weapon'), ('GN', 'Generic')], default='CN', max_length=300)),
                ('stat', models.CharField(max_length=100)),
                ('modifier', models.CharField(choices=[('+', 'Positive'), ('-', 'Negative'), ('*', 'Multiply'), ('0', 'None')], max_length=1)),
                ('effect', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GunMod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('stat', models.CharField(max_length=100)),
                ('modifier', models.CharField(choices=[('+', 'Positive'), ('-', 'Negative'), ('*', 'Multiply'), ('0', 'None')], max_length=1)),
                ('effect', models.IntegerField()),
                ('restriction', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GunSight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('stat', models.CharField(max_length=100)),
                ('modifier', models.CharField(choices=[('+', 'Positive'), ('-', 'Negative'), ('*', 'Multiply'), ('0', 'None')], max_length=1)),
                ('effect', models.IntegerField()),
                ('restriction', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('type', models.CharField(choices=[('WF', 'Worn Freighter'), ('RTT', 'Retired Troop Transport'), ('SAV', 'Strange Alien Vessel'), ('UPS', 'Upgraded Shuttle'), ('RSS', 'Retired Scout Ship'), ('RSV', 'Repurposed Science Vessel'), ('BMV', 'Battered Mining Ship'), ('UMC', 'Unreliable Merchant Cruiser'), ('FDV', 'Former Diplomatic Vessel'), ('ALC', 'Ancient Low-Tech Craft'), ('BSW', 'Built from Salvaged Wrecks'), ('RMS', 'Retired Military Patrol Ship')], max_length=200)),
                ('debt', models.CharField(max_length=4)),
                ('hull_points_max', models.CharField(max_length=5)),
                ('hull_points_cur', models.CharField(max_length=5)),
                ('traits', models.CharField(blank=True, max_length=500)),
                ('upgrades', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('equippable', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=600, null=True)),
                ('range', models.IntegerField(blank=True)),
                ('shots', models.IntegerField(blank=True)),
                ('dmg', models.IntegerField(blank=True)),
                ('mod', models.ManyToManyField(blank=True, to='crew_app.gunmod')),
                ('trait', models.ManyToManyField(blank=True, to='crew_app.equipmenttrait')),
            ],
        ),
        migrations.CreateModel(
            name='ProtectiveDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('SC', 'Screen'), ('AR', 'Armor')], default=None, max_length=200)),
                ('equippable', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=600, null=True)),
                ('trait', models.ManyToManyField(blank=True, to='crew_app.equipmenttrait')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('IM', 'Implant'), ('UD', 'Utility Device'), ('OI', 'On-board Items')], default=None, max_length=200)),
                ('equippable', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=600, null=True)),
                ('trait', models.ManyToManyField(blank=True, to='crew_app.equipmenttrait')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('CN', 'Consumable'), ('PR', 'Protective Device'), ('IM', 'Implant'), ('UD', 'Utility Device'), ('OI', 'On-board Items'), ('GM', 'Gun Mod'), ('GS', 'Gun Sight'), ('WP', 'Weapon')], default=None, max_length=200)),
                ('equippable', models.BooleanField()),
                ('stackable', models.BooleanField()),
                ('description', models.CharField(max_length=600, null=True)),
                ('range', models.IntegerField(blank=True)),
                ('shots', models.IntegerField(blank=True)),
                ('dmg', models.IntegerField(blank=True)),
                ('trait', models.ManyToManyField(blank=True, to='crew_app.equipmenttrait')),
            ],
        ),
        migrations.CreateModel(
            name='CrewRoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crew_name', models.CharField(max_length=200)),
                ('crew_origin_met', models.CharField(max_length=300)),
                ('crew_origin_description', models.CharField(max_length=300)),
                ('prev_campaigns', models.CharField(max_length=300)),
                ('crew_mates', models.ManyToManyField(to='crew_app.crewmate')),
                ('current_campaign', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crew_app.campaign')),
                ('ship_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crew_app.ship')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Consumable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('equippable', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=600, null=True)),
                ('trait', models.ManyToManyField(blank=True, to='crew_app.equipmenttrait')),
            ],
        ),
    ]
