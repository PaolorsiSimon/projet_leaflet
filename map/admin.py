from django import forms
from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import (
    PointInteret, Itineraire, PointDansItineraire, TypePointInteret, 
    Materiaux, Glossaire, Metier, Personnage, LienRenumar,
    PointDansGlossaire, ItineraireDansGlossaire, MetierDansGlossaire, 
    MateriauxDansPoint, MateriauxDansItineraire, PersonnageDansItineraire,
    LienRenumarPointInteret, LienRenumarItineraire
)

##pour point d'intérêt
class LienRenumarPointInteretInLine(admin.TabularInline):
    model = LienRenumarPointInteret
    extra = 1

class MateriauxDansPointInLine(admin.TabularInline):
    model = MateriauxDansPoint
    extra = 1

class PointDansGlossaireInLine(admin.TabularInline):
    model = PointDansGlossaire
    extra = 1

class PointInteretAdmin(LeafletGeoAdmin):
    inlines = [MateriauxDansPointInLine, LienRenumarPointInteretInLine, PointDansGlossaireInLine]

#pour itinéraire
class ItineraireDansGlossaireInLine(admin.TabularInline):
    model = ItineraireDansGlossaire
    extra = 1

class PointDansItineraireInline(admin.TabularInline):
    model = PointDansItineraire
    extra = 1

class MateriauxDansItineraireInline(admin.TabularInline):
    model = MateriauxDansItineraire
    extra = 1

class PersonnageDansItineraireInline(admin.TabularInline):
    model = PersonnageDansItineraire
    extra = 1

class LienRenumarItineraireInline(admin.StackedInline):
    model = LienRenumarItineraire
    extra = 1


class ItineraireAdmin(LeafletGeoAdmin):
    inlines = [PointDansItineraireInline, MateriauxDansItineraireInline, PersonnageDansItineraireInline, LienRenumarItineraireInline, ItineraireDansGlossaireInLine]
    list_display = ('depart', 'arrivee', 'commentaire')
    search_fields = ('depart', 'arrivee', 'commentaire')

class MetierDansGlossaireInLine(admin.TabularInline):
    model = MetierDansGlossaire
    extra = 1

class MetierAdmin(admin.ModelAdmin):
    inlines = [MetierDansGlossaireInLine]
    search_fields = ('nom',)

admin.site.register(Metier, MetierAdmin)
admin.site.register(Itineraire, ItineraireAdmin)
admin.site.register(PointInteret, PointInteretAdmin)
admin.site.register(Glossaire)
admin.site.register(Materiaux)
admin.site.register(Personnage)
admin.site.register(TypePointInteret)
admin.site.register(LienRenumar)
admin.site.register(PointDansItineraire)
