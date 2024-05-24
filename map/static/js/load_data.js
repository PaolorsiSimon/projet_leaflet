// Créer une couche de tuiles OpenStreetMap
var osmLayer = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

// Créer une couche de tuiles Cassini
// Créer une couche de tuiles Cassini
var cassiniLayer = L.tileLayer.wms('https://ws.sogefi-web.com/wms', {
    layers: 'Carte_Cassini',
    format: 'image/png', // Format d'image pris en charge
   // Spécifie si les images doivent être chargées avec un arrière-plan transparent
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

// Créer un contrôle de couches pour basculer entre les couches de tuiles

var pointsLayer = L.layerGroup();

var itinerairesLayer = L.layerGroup();

// Créer un objet pour stocker les couches de points en fonction de leur type
var pointsLayers = {};

// Fonction pour charger les données GeoJSON des points d'intérêt et les ajouter au groupe de calques
function chargerPointData(map) {
  // Charger les données GeoJSON à partir de l'URL '/pointsInteret_data'
  fetch(PointInteretDataUrl)
    .then((response) => response.json())
    .then((data) => {
      // Récupérer les données sur les types de points depuis l'URL 'typePoints_data'
      fetch('/typePoints_data')
        .then(response => response.json())
        .then(typeData => {
          // Pour chaque point, déterminez son type et ajoutez-le à la couche correspondante
          data.features.forEach(point => {
            var typeId = point.properties.type_point_interet;
            var typeName = typeData.find(type => type.pk === typeId).fields.type; // Récupérer le nom du type
            if (!pointsLayers[typeId]) {
              pointsLayers[typeId] = L.layerGroup(); // Créer une nouvelle couche si elle n'existe pas encore
              layersControl.addOverlay(pointsLayers[typeId], typeName, false); 
            }
            // Créer une couche GeoJSON à partir du point avec la fonctionnalité de clic
            var geojsonLayer = L.geoJSON(point, {
              onEachFeature: function (feature, layer) {
                layer.on('click', function () {
                  
                  afficherInfosPoint(feature.properties);
                });
              }
            });
            // Ajouter la couche GeoJSON à la couche correspondante dans l'objet pointsLayers
            geojsonLayer.addTo(pointsLayers[typeId]);
          });

          
          Object.values(pointsLayers).forEach(layer => {
            map.addLayer(layer);
          });
        })
        .catch(error => console.error("Erreur lors du chargement des données sur les types de points:", error));
    })
    .catch((error) => {
      console.error("Erreur lors du chargement des données GeoJSON:", error);
    });
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
          <p>Presentation : ${properties.presentation}</p>`;
      } else {
        console.error("Type de point non trouvé pour l'identifiant :", typeId);
      }
    })
    .catch(error => console.error("Erreur lors de la récupération des informations du type de point :", error));
}

function chargerItinerairesGeoJSON(map) {
  fetch('/itineraires_data/')
    .then((response) => response.json())
    .then((data) => {
      var geojsonLayer = L.geoJSON(data, {
        onEachFeature: function (feature, layer) {
          layer.on('click', function () {
            document.getElementById('info').innerHTML = `
              <h4>Informations sur l'itinéraire sélectionné :</h4>
              <p>Nom du départ : ${feature.properties.depart}</p>
              <p>Nom de l'arrivée : ${feature.properties.arrivee}</p>
              <p>Scenario : ${feature.properties.scenario}</p>
            `;
          });
        },
        style: function (feature) {
          return {
            color: "blue",
            weight: 3,
            opacity: 0.5,
          };
        },
      });

      geojsonLayer.addTo(itinerairesLayer);
    })
    .catch((error) => {
      console.error("Erreur lors du chargement des données GeoJSON des itinéraires:", error);
    });
}



chargerPointData(map);

chargerItinerairesGeoJSON(map);

var layersControl = L.control.layers(baseLayers, {
  "Itinéraires": itinerairesLayer.addTo(map)
}, { collapsed: false }).addTo(map);

