from django.urls import path

from map import views

app_name = 'map'

#AJOUTER URL POUR FRONT

urlpatterns = [
    path('map/', views.MapPageView.as_view(), name='map'),
    path('itineraires_data/', views.itineraires_dataset, name='itineraires_data'),
    path('pointsInteret_data/', views.pointsInteret_dataset, name='pointsInteret_data'),
    path('typePoints_data/', views.type_point_dataset, name='typePoints_data'),
#AJOUT POUR FRONT CI DESSOUS
    path('', views.home, name='home'),
    path('glossaire/', views.glossaire, name='glossaire'),
    path('liens/', views.liens, name='liens'),
    path('contacts/', views.contacts, name='contacts'),

    
    #path('glossaire/', views.FormulaireRecherche, name='FormulaireRecherche'), --> AJOUT FORMULAIRE NON CONLCUANT






  
]


