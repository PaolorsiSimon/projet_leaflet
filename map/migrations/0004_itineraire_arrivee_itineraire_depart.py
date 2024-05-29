# Generated by Django 5.0.3 on 2024-05-29 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_itineraire_commentaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='itineraire',
            name='arrivee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='arrivee_itineraires', to='map.pointinteret'),
        ),
        migrations.AddField(
            model_name='itineraire',
            name='depart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='depart_itineraires', to='map.pointinteret'),
        ),
    ]
