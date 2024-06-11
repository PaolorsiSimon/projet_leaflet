from django import forms
from django.contrib import admin
from flask import redirect
from leaflet.admin import LeafletGeoAdmin
from .models import (
    PointInteret, Itineraire, PointDansItineraire, TypePointInteret, 
    Materiaux, Glossaire, Metier, Personnage, LienRenumar,
    PointDansGlossaire, ItineraireDansGlossaire, MetierDansGlossaire, 
    MateriauxDansPoint, MateriauxDansItineraire, PersonnageDansItineraire,
    LienRenumarPointInteret, LienRenumarItineraire, LoireModel, CoursDeau
)


class CoursDeauAdmin(LeafletGeoAdmin):
    list_display=('gid',)

class LoireModelAdmin(LeafletGeoAdmin):
    list_display = ('nomentiteh',)

##pour point d'intérêt
class LienRenumarPointInteretInLine(admin.TabularInline):
    model = LienRenumarPointInteret
    extra = 1

class PointDansGlossaireInLine(admin.TabularInline):
    model = PointDansGlossaire
    extra = 1

class PointInteretAdmin(LeafletGeoAdmin):
    inlines = [LienRenumarPointInteretInLine, PointDansGlossaireInLine]
    search_fields = ('nom', 'presentation')
    list_filter = ('type_point_interet',)

#pour itinéraire
class ItineraireDansGlossaireInLine(admin.TabularInline):
    model = ItineraireDansGlossaire
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

#####################################################################################
class PointDansItineraireInline(admin.TabularInline):
    model = PointDansItineraire
    extra = 1
    ordering = ['positionDansItineraire']


class ItineraireAdmin(LeafletGeoAdmin):
    inlines = [PointDansItineraireInline, MateriauxDansItineraireInline, PersonnageDansItineraireInline, LienRenumarItineraireInline, ItineraireDansGlossaireInLine]
    list_display = ('depart', 'arrivee', 'commentaire')

    exclude = ('itineraire',)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Modification d'un objet existant
            return ['itineraire']
        return []

#####################################################################################

class MetierDansGlossaireInLine(admin.TabularInline):
    model = MetierDansGlossaire
    extra = 1

class MetierAdmin(admin.ModelAdmin):
    inlines = [MetierDansGlossaireInLine]
    search_fields = ('nom',)
    list_filter = ()

# pour glossaire
class GlossaireAdmin(admin.ModelAdmin):
    search_fields = ('mot', 'definition')
    list_filter = ()

# pour materiaux
class MateriauxAdmin(admin.ModelAdmin):
    search_fields = ('nom',)
    list_filter = ()

# pour personnage
class PersonnageAdmin(admin.ModelAdmin):
    search_fields = ('nom', 'prenom')
    list_filter = ('metiers_personnage',)

# pour type de point d'intérêt
class TypePointInteretAdmin(admin.ModelAdmin):
    search_fields = ('type',)
    list_filter = ()

# pour lien renumar
class LienRenumarAdmin(admin.ModelAdmin):
    search_fields = ('titre', 'commentaire')
    list_filter = ()

admin.site.register(Metier, MetierAdmin)
admin.site.register(CoursDeau, CoursDeauAdmin)

admin.site.register(Itineraire, ItineraireAdmin)
admin.site.register(LoireModel, LoireModelAdmin)

admin.site.register(PointInteret, PointInteretAdmin)
admin.site.register(Glossaire)
admin.site.register(Materiaux)
admin.site.register(Personnage)
admin.site.register(TypePointInteret)
admin.site.register(LienRenumar)
admin.site.register(PointDansItineraire)





