from django.contrib import admin
from django.apps import AppConfig

# Register your models here.
class PointsInteret(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pointsInteret'

class Itineraires(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'itineraires'