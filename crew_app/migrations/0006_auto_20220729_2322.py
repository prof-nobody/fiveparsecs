# Generated by Django 3.2.14 on 2022-07-30 03:22

import django.contrib.postgres.fields
import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crew_app', '0005_auto_20220729_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='crewmate',
            name='implants',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='ship',
            name='roll',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(null=True),
        ),
        migrations.AlterField(
            model_name='background',
            name='roll',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(null=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='roll',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(null=True),
        ),
        migrations.AlterField(
            model_name='crewmate',
            name='background',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crew_app.background'),
        ),
        migrations.AlterField(
            model_name='crewmate',
            name='crew_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crew_app.class'),
        ),
        migrations.AlterField(
            model_name='crewmate',
            name='motivation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crew_app.motivation'),
        ),
        migrations.AlterField(
            model_name='motivation',
            name='roll',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(null=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='traits',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='ship',
            name='upgrades',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None),
        ),
    ]
