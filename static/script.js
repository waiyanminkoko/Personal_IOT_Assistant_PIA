// Get data from IoT devices
function getIoTData() {
    // Code to get data from IoT devices
  }
  
  // Update dashboard with IoT data
/*function updateDashboard() {
    var temp = getIoTData("temp");
    var humidity = getIoTData("humidity");
    var rfid = getIoTData("rfid");
    var door = getIoTData("door");
    var stats = getIoTData("stats");
    var song = getIoTData("song");
    var album = getIoTData("album");
  
    document.getElementById("temp").innerHTML = temp + "°C";
    document.getElementById("humidity").innerHTML = humidity + "%";
    document.getElementById("rfid").innerHTML = rfid;
    document.getElementById("door").innerHTML = door;
    document.getElementById("stats").innerHTML = stats;
    document.getElementById("song-name").innerHTML = song;
    document.getElementById("album-cover").src = album;
  
    // Get value of fan speed slider and update IoT device
    var fanSpeed = document.getElementById("fan-speed").value;
    setIoTData("fanSpeed", fanSpeed);
  
    // Get state of light switch and update IoT device
    var light = document.getElementById("light-switch").value;
    setIoTData("light", light);
  
    // Get state of curtain switch and update IoT device
    var curtain = document.getElementById("curtain-switch").value;
    setIoTData("curtain", curtain);

    // Get current song and update IoT device
    var music = document.getElementById("music-player").currentSrc;
    setIoTData("music", music);
  
  }*/
//Light Switch 
function light_switch() {
  const toggle = document.querySelector('.lightswitch');

  if (toggle) {
    toggle.addEventListener('change', function(event) {
      const isChecked = event.target.checked;
      fetch('http://0.0.0.0:5000/lightswitch', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          state: isChecked
        })
      });
    });
  } 

  else {
    console.error('Element with class .lightswitch not found');
  }
}





//Fan Speed
const range = document.querySelector('#fan_speed');

range.addEventListener('input', function(event) {
  const speed = event.target.value;
  fetch('/fanspeed', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      speed: speed
    })
  });
});

  // Call updateDashboard function every 5 seconds
  setInterval(updateDashboard, 5000);