
=======
#POUR WINDOWS
Importer le projet dans l'environnement Django, faire la commande : git clone "lien_du_projet"
Ensuite, si ce n'est pas fait, installer PgAdmin4, apres installation, ouvrir l'application stackbulder de pgadmin4, selectionner l'option PostGis dans spatial extension .
Créer une bdd vide, nommée "projet_leaflet" et ajouter extension postgis dans la bdd, dans extension -> create -> postgis
installer requirements_leaflet.txt, verifier si l'installation est effectuée correctement
pour inserer les données effectuer la commande suivante : psql -U postgres -d ma_bdd -f backupfile.sql

#POUR MAC
installer PgAdmin4, apres installation, ouvrir l'application stackbulder de pgadmin4, selectionner l'option PostGis dans spatial extension .
Créer une bdd vide, nommée "projet_leaflet" et ajouter extension postgis dans la bdd, dans extension -> create -> postgis
installer rq_mac.txt, verifier si l'installation est effectuée correctement
pour inserer les données effectuer la commande suivante : psql -U postgres -d ma_bdd -f backupfile.sql
