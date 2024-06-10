from django import forms
from map.models import Metier, Personnage, Materiaux

#VERIFIER LES IMPORTS POUR LA RECHERCHE GLOSSAIRE

class FormulaireRecherche(forms.Form): # --> Cette partie pose soucis ???? Voir message erreur terminal
    mot = forms.CharField(label = 'Mot à rechercher', required=True)
