

var coordinates = {
  "coordinates": [
    [85.31732829466324, 27.709944374495038],
    [85.3173734783893, 27.710407250753548],
    [85.31746384583948, 27.710778693243682],
    [85.31756712292753, 27.711270138286892],
    [85.31760585183565, 27.71168729338882],
    [85.3176574903797, 27.712173019921494],
    [85.31777367710185, 27.712790175219453],
    [85.31783177046395, 27.713144466497823],
    [85.31732829464136, 27.713361612252385],
    [85.31633425260827, 27.713504471101288],
    [85.31568877081332, 27.71361875798769],
    [85.31544994254898, 27.71369304439935],
    [85.31534021064283, 27.713430184560337],
    [85.31527566246274, 27.713013036123982],
    [85.31515302092248, 27.712601600487915],
    [85.31510783719648, 27.712041588377076],
    [85.31499810529033, 27.711595862397047],
    [85.31490128302028, 27.711104418821392],
    [85.31480446075204, 27.71052725551617],
    [85.31475927702593, 27.710035807126076],
    [85.31507556310646, 27.70995008915628],
    [85.31570813526741, 27.709887229269768],
    [85.31585659607958, 27.709887229269768]
  ]
}

var coordinateArray = coordinates.coordinates;

var map = L.map('map').setView([27.709944374495038, 85.31732829466324], 16);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

var marker = L.marker(coordinateArray[0]).addTo(map);

var index = 1;

function updateMarker() {
  if (index < coordinateArray.length) {
    var coordinate = coordinateArray[index];
    marker.setLatLng([coordinate[1], coordinate[0]]);
    index++;
  } else {
    clearInterval(intervalId); // Stop updating when all coordinates are covered
  }
}

// Update marker every 1000 milliseconds (1 second)
var intervalId = setInterval(updateMarker, 1000);
