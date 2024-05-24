// Créer une couche de tuiles OpenStreetMap
var osmLayer = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

// Créer une couche de tuiles Cassini
var cassiniLayer = L.tileLayer.wms('https://ws.sogefi-web.com/wms', {
  layers: 'Carte_Cassini',
  format: 'image/png'
});

// Créer une carte avec la couche de tuiles OpenStreetMap comme vue par défaut
var map = L.map("map", {
  layers: [osmLayer] // Utiliser la couche de tuiles OpenStreetMap comme vue par défaut
}).setView([47.399452334950986, 0.6850264790425225], 11);

// Ajouter les deux couches de tuiles à un contrôle de couches pour permettre à l'utilisateur de basculer entre elles
var baseLayers = {
  "OpenStreetMap": osmLayer,
  "Carte Cassini": cassiniLayer
};

var layersControl = L.control.layers(baseLayers, {}, { collapsed: false }).addTo(map);

var pointsLayer = L.layerGroup().addTo(map); // Couche de points d'intérêt
var itinerairesLayer = L.layerGroup().addTo(map); // Couche d'itinéraires

// Fonction pour charger les données GeoJSON des points d'intérêt et les ajouter au groupe de calques
function chargerPointData() {
  fetch('/pointsInteret_data')
    .then(response => response.json())
    .then(data => {
      data.features.forEach(point => {
        var geojsonLayer = L.geoJSON(point, {
          onEachFeature: function (feature, layer) {
            layer.on('click', function () {
              afficherInfosPoint(feature.properties);
            });
          }
        });

        geojsonLayer.addTo(pointsLayer);
      });
    })
    .catch(error => console.error("Erreur lors du chargement des données GeoJSON:", error));
}

// Fonction pour afficher les informations d'un point au clic
function afficherInfosPoint(properties) {
  var typeId = properties.type_point_interet;
  fetch('/typePoints_data')
    .then(response => response.json())
    .then(data => {
      const typePoint = data.find(type => type.pk === typeId);
      if (typePoint) {
        document.getElementById('info').innerHTML = `
          <h4>Informations sur le point sélectionné :</h4>
          <p>Nom : ${properties.nom}</p>
          <p>Type : ${typePoint.fields.type}</p>
          <p>Présentation : ${properties.presentation}</p>`;
      } else {
        console.error("Type de point non trouvé pour l'identifiant :", typeId);
      }
    })
    .catch(error => console.error("Erreur lors de la récupération des informations du type de point :", error));
}

// Fonction pour charger les données GeoJSON des itinéraires et les ajouter au groupe de calques
function chargerItinerairesGeoJSON() {
    fetch('/itineraires_data')
      .then(response => response.json())
      .then(data => {
        data.features.forEach(itineraire => {
          var geojsonLayer = L.geoJSON(itineraire, {
            onEachFeature: function (feature, layer) {
              layer.on('click', function () {
                afficherInfosItineraire(feature.properties);
              });
            },
            style: function () {
              return {
                color: "blue",
                weight: 3,
                opacity: 0.5
              };
            }
          });
  
          geojsonLayer.addTo(itinerairesLayer);
        });
      })
      .catch(error => console.error("Erreur lors du chargement des données GeoJSON des itinéraires:", error));
  }


  // Fonction pour afficher les informations d'un point d'intérêt au clic
  function afficherInfosPoint(properties) {
    document.getElementById('info').innerHTML = `
      <h4>Informations sur le point d'intérêt sélectionné :</h4>
      <p>Nom : ${properties.nom}</p>
      <p>Présentation : ${properties.presentation}</p>
      <p>Type de point d'intérêt : ${properties.type_point_interet}</p>`;
  }
  
  chargerPointData();
  chargerItinerairesGeoJSON();
  