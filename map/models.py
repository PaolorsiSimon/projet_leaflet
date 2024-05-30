from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
from django.core.exceptions import ValidationError

##test


class PointInteret(models.Model):
    # Distinguer le nom unique, ajouter un help texte
    nom = models.CharField(
        max_length=255,
        unique=True,
        help_text="Nom unique du point d'intérêt"
    )
    point = models.PointField()
    presentation = models.TextField()
    type_point_interet = models.ForeignKey(
        'TypePointInteret',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = "Points d'intérêt"

class Itineraire(models.Model):
    itineraire = models.LineStringField()
    scenario = models.TextField()
    commentaire = models.TextField(help_text="Commentaire sur l'itinéraire", null=True)
#mettre commentaire pas obligatoire

    class Meta:
        verbose_name_plural = "Itinéraires"
    
    #passer par la table intermediare pour les points
    @property
    def depart(self):
        first_point = self.points_ordre.first()
        return first_point.fk_pointInteret.nom if first_point else None

    @property
    def arrivee(self):
        last_point = self.points_ordre.last()
        return last_point.fk_pointInteret.nom if last_point else None

    @property
    def points_ordre(self):
        return self.points.all().order_by('positionDansItineraire')


# ---------- ICI TOUTE LES CLASSES PRINCIPALES -----------
class TypePointInteret(models.Model):
    type = models.CharField(
        max_length=255
    )
    #ajouter help_text
    description = models.TextField(help_text="Ajouter une description.",default='description du type') # Description facultative

    def __str__(self):
        return self.type
    
    class Meta:
        verbose_name_plural = "Types de point d'intérêt"
        constraints=[
            models.UniqueConstraint(fields=['type'], name='unique_typePoint')
        ]
    def clean(self):
        super().clean() #ici pour checker en lower

        self.type = self.type.lower()
        #a revoir pour faire attention a la casse
    


class Materiaux(models.Model):
    nom=models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Materiaux"
    def __str__(self):
        return self.nom



class Glossaire(models.Model):
    mot=models.CharField(max_length=255, help_text="Ajoutez ce mot uniquement s'il appartient à la présentation d'un point d'intérêt.")
    definition = models.TextField()

    class Meta:
        verbose_name_plural = "Glossaire"
        constraints=[
            models.UniqueConstraint(fields=['mot'], name='unique_motGlossaire')
        ]
    def clean(self):
        super().clean() #ici pour checker en lower

        self.mot = self.mot.lower()

    def __str__(self):
        return self.mot


class Metier(models.Model):
    nom=models.CharField(max_length=255)
    #mettre commentaire pas obligatoire
    description = models.TextField()
    class Meta:
        verbose_name_plural = "Metiers"

    def clean(self):
        super().clean() #ici pour checker en lower

        self.nom = self.nom.lower()
    def __str__(self):
        return self.nom

class Personnage(models.Model):
    nom=models.CharField(max_length=255, null=True)
    prenom=models.CharField(max_length=255, null=True)

    metiers_personnage = models.ForeignKey(
        Metier,
        on_delete=models.SET_NULL,
        null=True
    )
    class Meta:
        verbose_name_plural = "Personnages"
        constraints=[
            models.UniqueConstraint(fields=['prenom','nom'], name='unique_nomPrenom')
        ]
    def clean(self):
        super().clean() #ici pour checker en lower

        self.nom = self.nom.lower()
        self.prenom = self.prenom.lower()

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
class LienRenumar(models.Model):
    #ajout de titre
    titre= models.CharField(max_length=255, default='lien renumar')
    lien = models.URLField()
    #mettre commentaire pas obligatoire
    commentaire = models.TextField(null=True)
    
    def __str__(self):
        return self.titre


# ---------- ICI TOUTE LES CLASSES SECONDAIRES, liaisons entre les clases principales -----------


### les liens vers le glossaire 
class PointDansGlossaire(models.Model):
    #ajouter un help text pour bien prevnir qu'un mot de glossaire n'est ajouter que si il appartient a la presentation de point d'interet
    fk_pointInteret = models.ForeignKey('PointInteret', models.CASCADE, help_text="Sélectionnez le point d'intérêt correspondant.")
    fk_glossaire = models.ForeignKey('Glossaire', models.CASCADE, help_text="Ajoutez ce mot uniquement s'il appartient à la présentation du point d'intérêt sélectionné.")

    def __str__(self):
        return f'{self.fk_pointInteret}/{self.fk_glossaire}'

    class Meta :
        verbose_name = 'point/glossaire'
        constraints=[
            models.UniqueConstraint(fields=['fk_pointInteret','fk_glossaire'], name='unique_pointDansGlossaire')
        ]   

class ItineraireDansGlossaire(models.Model):
    #ajouter un help text pour bien prevnir qu'un mot de glossaire n'est ajouter que si il appartient au scenario

    fk_itineraire = models.ForeignKey('Itineraire', models.CASCADE, help_text="Sélectionnez l'itinéraire correspondant.")
    fk_glossaire = models.ForeignKey('Glossaire', models.CASCADE, help_text="Ajoutez ce mot uniquement s'il appartient à la description de l'itinéraire sélectionné.")

    def __str__(self):
        return f'{self.fk_itineraire}/{self.fk_glossaire}'

    class Meta :
        verbose_name = 'itineraire/glossaire'
        constraints=[
            models.UniqueConstraint(fields=['fk_itineraire','fk_glossaire'], name='unique_itineraireDansGlossaire')
        ]   
        

class MetierDansGlossaire(models.Model):
    fk_metier = models.ForeignKey('Metier', models.CASCADE)
    fk_glossaire = models.ForeignKey('Glossaire', models.CASCADE)

    def __str__(self):
        return f'{self.fk_metier}/{self.fk_glossaire}'

    class Meta :
        verbose_name = 'metier/glossaire'
        constraints=[
            models.UniqueConstraint(fields=['fk_metier','fk_glossaire'], name='unique_metierDansGlossaire')
        ]


##liens vers point et itineraire

class PointDansItineraire(models.Model):
    fk_pointInteret = models.ForeignKey('PointInteret', models.CASCADE)
    fk_itineraire = models.ForeignKey('Itineraire', models.CASCADE, related_name="points")
    positionDansItineraire = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['fk_pointInteret', 'fk_itineraire',], name='unique_pointDansItineraire'),
            models.UniqueConstraint(fields=['fk_itineraire', 'positionDansItineraire'], name='unique_positionDansItineraire')

        ]
        ordering = ['positionDansItineraire']
    
    def __str__(self):
        return f"{self.fk_pointInteret} à la position {self.positionDansItineraire} dans {self.fk_itineraire}"



class MateriauxDansPoint(models.Model):
    fk_materiaux = models.ForeignKey('Materiaux', models.CASCADE)
    fk_pointInteret = models.ForeignKey('PointInteret', models.CASCADE)

    def __str__(self):
        return f'{self.fk_pointInteret}/{self.fk_materiaux}'

    class Meta :
        verbose_name_plural = 'points/materiaux'
        verbose_name = 'point/materiaux'
        constraints=[
            models.UniqueConstraint(fields=['fk_pointInteret','fk_materiaux'], name='unique_materiauxDansPoint')
        ]



class MateriauxDansItineraire(models.Model):
    fk_itineraire = models.ForeignKey('Itineraire', models.CASCADE)
    fk_materiaux = models.ForeignKey('Materiaux', models.CASCADE)
    #mettre commentaire pas obligatoire
    commentaire = models.TextField(
        null=True,
        help_text="Ajouter si l'information est disponible la quantité et la valeur"
        )

class PersonnageDansItineraire(models.Model):
    fk_itineraire = models.ForeignKey('Itineraire', models.CASCADE)
    fk_personnage = models.ForeignKey('Personnage', models.CASCADE)

    contraintes = [
            models.UniqueConstraint(fields=['fk_itineraire','fk_personnage'], name='unique_personnageDansItineraire')

    ]

class LienRenumarPointInteret(models.Model):
    point_interet = models.ForeignKey(PointInteret, on_delete=models.CASCADE)
    lien_renumar = models.ForeignKey(LienRenumar, on_delete=models.SET_NULL, null=True)
#ajout contrainte sur liens pour n'avoir q'une seule fois le meme lien
    def __str__(self):
        return f'{self.point_interet} - {self.lien_renumar}'

    class Meta:
        verbose_name = 'Lien Renumar/Point d\'Intérêt'
        constraints = [
            models.UniqueConstraint(fields=['point_interet', 'lien_renumar'], name='unique_lien_renumar_point_interet')
        ]

class LienRenumarItineraire(models.Model):
    itineraire = models.ForeignKey(Itineraire, on_delete=models.CASCADE)
    lien_renumar = models.ForeignKey(LienRenumar, on_delete=models.SET_NULL, null=True)
#ajout contrainte sur lien pour n'avoir qu'une seule fois le meme lien
    def __str__(self):
        return f'{self.itineraire} - {self.lien_renumar}'

    class Meta:
        verbose_name = 'Lien Renumar/Itinéraire'
        constraints = [
            models.UniqueConstraint(fields=['itineraire', 'lien_renumar'], name='unique_lien_renumar_itineraire')
        ]

