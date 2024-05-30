from django import forms
from map.models import Metier, Personnage, Materiaux

#VERIFIER LES IMPORTS POUR LA RECHERCHE GLOSSAIRE

class FormulaireRecherche(forms.Form):
    mot = forms.CharField(label = 'Mot à rechercher', required=True)
