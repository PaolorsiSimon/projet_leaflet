# Generated by Django 5.0.3 on 2024-05-15 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_glossaire_materiaux_metiers_typequantite_typevaleur_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Metiers',
            new_name='Metier',
        ),
        migrations.RenameModel(
            old_name='Personnages',
            new_name='Personnage',
        ),
        migrations.AlterModelOptions(
            name='glossaire',
            options={'verbose_name': 'Glossaire'},
        ),
        migrations.AlterModelOptions(
            name='itineraire',
            options={'verbose_name': 'Itineraires'},
        ),
        migrations.AlterModelOptions(
            name='materiaux',
            options={'verbose_name': 'Materiaux'},
        ),
        migrations.AlterModelOptions(
            name='metier',
            options={'verbose_name': 'Metiers'},
        ),
        migrations.AlterModelOptions(
            name='personnage',
            options={'verbose_name': 'Personnages'},
        ),
        migrations.AlterModelOptions(
            name='pointinteret',
            options={'verbose_name': "Points d'intérêt"},
        ),
        migrations.AlterModelOptions(
            name='typepointinteret',
            options={'verbose_name': "Types de point d'intérêt"},
        ),
        migrations.AlterModelOptions(
            name='typequantite',
            options={'verbose_name': 'Types de quantité'},
        ),
        migrations.AlterModelOptions(
            name='typevaleur',
            options={'verbose_name': 'Types de valeur'},
        ),
    ]