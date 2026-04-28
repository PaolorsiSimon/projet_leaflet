# Guide de setup LINUX — projet_leaflet (Django + Leaflet + PostGIS)

> Testé sur **Linux (Ubuntu/Debian)** avec Python et pip déjà installés.

---

## 1. Cloner le projet

```bash
git clone https://github.com/PaolorsiSimon/projet_leaflet.git
cd projet_leaflet
```

---

## 2. Installer PostgreSQL + PostGIS

```bash
sudo apt update
sudo apt install -y postgresql postgresql-contrib postgis
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

---

## 3. Créer la base de données

```bash
sudo -u postgres psql <<EOF
CREATE USER user WITH PASSWORD 'root';
CREATE DATABASE projet_leaflet OWNER user;
\c projet_leaflet
CREATE EXTENSION postgis;
EOF
```

> Remplace `user` et `root` par l'utilisateur et le mot de passe de ton choix,
> et répercute ces valeurs dans `projet_leaflet/settings.py`.

---

## 4. Créer le virtualenv et installer les dépendances

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements_leaflet.txt
```

---

## 5. Configurer la base de données dans Django

Dans `projet_leaflet/settings.py`, vérifier que la section `DATABASES` est bien :

```python
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "HOST": "localhost",
        "NAME": "projet_leaflet",
        "PASSWORD": "root",       # ton mot de passe
        "USER": "user",            # ton utilisateur
    }
}
```

---

## 6. Générer et appliquer les migrations

Le dossier `map/migrations/` est vide dans le dépôt : il faut générer les migrations
de l'app `map` avant de les appliquer.

```bash
# Migrations Django de base (auth, admin, sessions…)
python manage.py migrate

# Génération des migrations de l'app map
python manage.py makemigrations map

# Application des migrations map
python manage.py migrate
```

---

## 7. Importer le backup

Une fois toutes les tables créées, importer les données :

```bash
sudo -u postgres psql -d projet_leaflet < backupfile.sql
```

Les messages `SET` et `(1 row)` sont normaux et inoffensifs.

---

## 8. Lancer le serveur

```bash
python manage.py runserver
```

Ouvrir http://127.0.0.1:8000 dans le navigateur.


---

## Récapitulatif des commandes en une fois

```bash
git clone https://github.com/PaolorsiSimon/projet_leaflet.git
cd projet_leaflet

sudo apt update && sudo apt install -y postgresql postgresql-contrib postgis
sudo systemctl start postgresql

sudo -u postgres psql -c "CREATE USER user WITH PASSWORD 'root';"
sudo -u postgres psql -c "CREATE DATABASE projet_leaflet OWNER user;"
sudo -u postgres psql -d projet_leaflet -c "CREATE EXTENSION postgis;"

python3 -m venv venv && source venv/bin/activate
pip install -r requirements_leaflet.txt

python manage.py migrate
python manage.py makemigrations map
python manage.py migrate

sudo -u postgres psql -d projet_leaflet < backupfile.sql

python manage.py runserver
```



=======
# POUR WINDOWS - obselète
Importer le projet dans l'environnement Django, faire la commande : git clone "lien_du_projet"
Ensuite, si ce n'est pas fait, installer PgAdmin4, apres installation, ouvrir l'application stackbulder de pgadmin4, selectionner l'option PostGis dans spatial extension .
Créer une bdd vide, nommée "projet_leaflet" et ajouter extension postgis dans la bdd, dans extension -> create -> postgis
installer requirements_leaflet.txt, verifier si l'installation est effectuée correctement
pour la base de données : 
  - aller dans le fichier settings.py, puis rechercher "mot_de_passe", a cette ligne il faudra changer le mot de passe "root" par votre mot de passe pgadmin
  - créer une migration "python manage.py makemigrations", puis executer la avecv "python manage.py migrate", cela va créer les tables de notre base de données
  - pour inserer les données effectuer la commande suivante : psql -U postgres -d ma_bdd -f backupfile.sql


# POUR MAC - obselète
installer PgAdmin4, apres installation, ouvrir l'application stackbulder de pgadmin4, selectionner l'option PostGis dans spatial extension .
Créer une bdd vide, nommée "projet_leaflet" et ajouter extension postgis dans la bdd, dans extension -> create -> postgis
installer rq_mac.txt, verifier si l'installation est effectuée correctement
pour la base de données : 
  - aller dans le fichier settings.py, puis rechercher "mot_de_passe", a cette ligne il faudra changer le mot de passe "root" par votre mot de passe pgadmin
  - créer une migration "python manage.py makemigrations", puis executer la avecv "python manage.py migrate", cela va créer les tables de notre base de données
  - pour inserer les données effectuer la commande suivante : psql -U postgres -d projet_leaflet -f backupfile.sql
