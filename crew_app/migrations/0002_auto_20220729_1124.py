# Generated by Django 3.2.14 on 2022-07-29 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crew_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(choices=[('BH', 'Baseline Human'), ('EN', 'Engineer'), ('KE', "K'Erin"), ('SL', 'Soulless'), ('PC', 'Precursor'), ('FL', 'Feral'), ('SW', 'Swift'), ('DC', 'De-Converted'), ('UA', 'Unity Agent'), ('MP', 'Mysterious Past'), ('HA', 'Hakshan'), ('ST', 'Stalker'), ('HU', 'Hulker'), ('HR', 'Hopeful Rookie'), ('GU', 'Genetic Uplift'), ('MU', 'Mutant'), ('AB', 'Assault Bot'), ('MA', 'Manipulator'), ('PR', 'Primitive'), ('FE', 'Feeler'), ('ES', 'Emo-Suppressed'), ('MI', 'Minor Alien'), ('TR', 'Traveler'), ('EM', 'Empath'), ('BU', 'Bio-upgrade')], default='BH', max_length=200)),
                ('reactions', models.CharField(max_length=30)),
                ('speed', models.CharField(max_length=30)),
                ('combat_skill', models.CharField(max_length=30)),
                ('toughness', models.CharField(max_length=30)),
                ('savvy', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='crewmate',
            name='combat_skill',
        ),
        migrations.RemoveField(
            model_name='crewmate',
            name='reactions',
        ),
        migrations.RemoveField(
            model_name='crewmate',
            name='savvy',
        ),
        migrations.RemoveField(
            model_name='crewmate',
            name='speed',
        ),
        migrations.RemoveField(
            model_name='crewmate',
            name='toughness',
        ),
        migrations.AlterField(
            model_name='crewmate',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crew_app.species'),
        ),
    ]
