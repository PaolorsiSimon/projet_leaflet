# Generated by Django 5.0.3 on 2024-05-29 17:52

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_delete_coursdeau'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursDeau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo_point_2d', models.CharField(max_length=255)),
                ('id_coursDeau', models.CharField(max_length=255)),
                ('prec_plani', models.FloatField()),
                ('prec_alti', models.FloatField()),
                ('artif', models.CharField(max_length=255)),
                ('fictif', models.CharField(max_length=255)),
                ('franchisst', models.CharField(max_length=255)),
                ('nom', models.CharField(max_length=255)),
                ('pos_sol', models.CharField(max_length=255)),
                ('regime', models.CharField(max_length=255)),
                ('z_ini', models.FloatField()),
                ('z_fin', models.FloatField()),
                ('commune', models.CharField(max_length=255)),
                ('code_insee', models.CharField(max_length=255)),
                ('epci_name', models.CharField(max_length=255)),
                ('dep_name', models.CharField(max_length=255)),
                ('reg_name', models.CharField(max_length=255)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
            ],
        ),
    ]
