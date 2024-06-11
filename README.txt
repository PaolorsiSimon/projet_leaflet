
installer osgeo4w / pour mac, voir la doc
installer requirements_leaflet.txt
ouvrir stackbuilder et ajouter postgis
ajouter extension postgis dans la bdd
verifier chemin et version de gdal, on utilise la version 308
=======
#POUR WINDOWS
apres importation du projet, il faut installer Osgeo4w, ne pas changer les parametres de telechargement et le repertoire de destination de l'installation
Ensuite, si ce n'est pas fait, installer PgAdmin4, apres installation, ouvrir l'application stackbulder de pgadmin4, selectionner l'option PostGis dans spatial extension .
Créer une bdd vide, nommée "projet_leaflet" et ajouter extension postgis dans la bdd, dans extension -> create -> postgis
installer requirements_leaflet.txt, verifier si l'installation est effectuée correctement
verifier chemin et version de gdal,  gdal se trouve dans le dossier osgeo4w, on utilise la version 308, si différente, changer la vresion dans les settings

#POUR MAC
installer PgAdmin4, apres installation, ouvrir l'application stackbulder de pgadmin4, selectionner l'option PostGis dans spatial extension .
Créer une bdd vide, nommée "projet_leaflet" et ajouter extension postgis dans la bdd, dans extension -> create -> postgis
installer rq_mac.txt, verifier si l'installation est effectuée correctement
verifier chemin et version de gdal,  gdal se trouve dans le dossier osgeo4w, on utilise la version 308, si différente, changer la vresion dans les settings
