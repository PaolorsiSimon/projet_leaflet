# Guide de setup — projet_leaflet (Django + Leaflet + PostGIS)

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
CREATE USER spa WITH PASSWORD 'root';
CREATE DATABASE projet_leaflet OWNER spa;
\c projet_leaflet
CREATE EXTENSION postgis;
EOF
```

> Remplace `spa` et `root` par l'utilisateur et le mot de passe de ton choix,
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
        "USER": "spa",            # ton utilisateur
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

sudo -u postgres psql -c "CREATE USER spa WITH PASSWORD 'root';"
sudo -u postgres psql -c "CREATE DATABASE projet_leaflet OWNER spa;"
sudo -u postgres psql -d projet_leaflet -c "CREATE EXTENSION postgis;"

python3 -m venv venv && source venv/bin/activate
pip install -r requirements_leaflet.txt

python manage.py migrate
python manage.py makemigrations map
python manage.py migrate

sudo -u postgres psql -d projet_leaflet < backupfile.sql

python manage.py runserver
```