
=======
#POUR WINDOWS
Importer le projet dans l'environnement Django, faire la commande : git clone "lien_du_projet"
Ensuite, si ce n'est pas fait, installer PgAdmin4, apres installation, ouvrir l'application stackbulder de pgadmin4, selectionner l'option PostGis dans spatial extension .
Créer une bdd vide, nommée "projet_leaflet" et ajouter extension postgis dans la bdd, dans extension -> create -> postgis
installer requirements_leaflet.txt, verifier si l'installation est effectuée correctement
pour la base de données : 
  - aller dans le fichier settings.py, puis rechercher "mot_de_passe", a cette ligne il faudra changer le mot de passe "root" par votre mot de passe pgadmin
  - créer une migration "python manage.py makemigrations", puis executer la avecv "python manage.py migrate", cela va créer les tables de notre base de données
  - pour inserer les données effectuer la commande suivante : psql -U postgres -d ma_bdd -f backupfile.sql


#POUR MAC
installer PgAdmin4, apres installation, ouvrir l'application stackbulder de pgadmin4, selectionner l'option PostGis dans spatial extension .
Créer une bdd vide, nommée "projet_leaflet" et ajouter extension postgis dans la bdd, dans extension -> create -> postgis
installer rq_mac.txt, verifier si l'installation est effectuée correctement
pour la base de données : 
  - aller dans le fichier settings.py, puis rechercher "mot_de_passe", a cette ligne il faudra changer le mot de passe "root" par votre mot de passe pgadmin
  - créer une migration "python manage.py makemigrations", puis executer la avecv "python manage.py migrate", cela va créer les tables de notre base de données
  - pour inserer les données effectuer la commande suivante : psql -U postgres -d projet_leaflet -f backupfile.sql



#POUR ACCEDER A ADMIN
nom admin : admin
mot de passe : K1SIpaC1
