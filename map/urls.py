from django.urls import path

from map import views

app_name = 'map'

urlpatterns = [
    path('', views.MapPageView.as_view(), name='map'),
    path('itineraires_data/', views.itineraires_dataset, name='itineraires_data'),
    path('pointsInteret_data/', views.pointsInteret_dataset, name='pointsInteret_data'),
    path('typePoints_data/', views.type_point_dataset, name='typePoints_data'),



    
]


