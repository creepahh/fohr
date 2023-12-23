const chatSocket = new WebSocket("ws://" + window.location.host + "/ws/chat/");

chatSocket.onmessage = function (e) {
  const data = JSON.parse(e.data);
  const message = data["message"];
  console.log(message);
};

chatSocket.onclose = function (e) {
  console.error("Chat socket closed unexpectedly");
};

function sendMessage(message) {
  chatSocket.send(
    JSON.stringify({
      message: message,
    })
  );
}

var map = L.map("map").setView([27.709944374495038, 85.31732829466324], 13);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

L.marker([27.709944374495038, 85.31732829466324])
  .addTo(map)
  .bindPopup("A pretty CSS popup.<br> Easily customizable.")
  .openPopup();
