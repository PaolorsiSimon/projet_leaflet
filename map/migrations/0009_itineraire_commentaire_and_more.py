# Generated by Django 5.0.3 on 2024-05-23 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_lienrenumar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itineraire',
            name='commentaire',
            field=models.TextField(help_text="Commentaire sur l'itinéraire", null=True),
        ),
        migrations.AlterField(
            model_name='materiauxdansitineraire',
            name='commentaire',
            field=models.TextField(help_text="Ajouter si l'information est disponible la quantité et la valeur", null=True),
        ),
    ]
