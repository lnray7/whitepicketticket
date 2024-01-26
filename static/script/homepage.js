const API_KEY = "AIzaSyBdPYyaT-s6ha5WXv8rEBalylzXx2iPEUk";
let map = null;

const initMap = () => {
  const sf = { lat: 37.7606508, lng: -122.4739392 };
  // The map, centered at Uluru
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 13,
    center: sf,
    disableDefaultUI: true,
  });
};

let markers = [];
const addressButton = document.getElementById("address-button");
const addressBox = document.getElementById("address-input");

addressButton.addEventListener("click", () => {
  const params = new URLSearchParams({
    address: addressBox.value,
    citations: true,
    meters: true,
  });
  fetch(`/api/parking_data?${params.toString()}`)
    .then((r) => r.json())
    .then((data) => {
      console.log(data);
      // Remove all markers from the map
      markers.forEach((marker) => marker.setMap(null));
      markers = [];

      // Create citation markers and info windows
      for (let citation of data.citations) {
        const marker = new google.maps.Marker({
          position: { lat: citation.lat, lng: citation.lon },
          title: citation.citation_location,
          map: map,
          icon: {
            url: "/static/images/blue-ticket.png",
            scaledSize: {
              width: 50,
              height: 50,
            },
          },
        });

        const infoWindow = new google.maps.InfoWindow({
          content: `${citation.citation_location}<br>Fine Amount: $${citation.fine_amount.toFixed(2)}<br>Date Added: ${citation.citation_issued_at}`,
        });

        marker.addListener("click", () => {
          infoWindow.open(map, marker);
        });

        markers.push(marker);
      }

      // Create meter marker and info window
      const meter = new google.maps.Marker({
        position: { lat: data.min_meter.lat, lng: data.min_meter.lon },
        title: data.min_meter.street_id + data.min_meter.street_name,
        map: map,
        icon: {
          url: "/static/images/red-meter-marker.png",
          scaledSize: {
            width: 50,
            height: 50,
          },
        },
      });

      const infoWindow = new google.maps.InfoWindow({
        content: data.min_meter.street_id + data.min_meter.street_name,
      });

      meter.addListener("click", () => {
        infoWindow.open(map, meter);
      });

      markers.push(meter);

      // Create user marker
      new google.maps.Marker({
        position: { lat: data.search_coords.lat, lng: data.search_coords.lon },
        title: data.search_coords.lat + data.search_coords.lon,
        map: map,
        icon: {
          url: "/static/images/icons8-map-pin-48.png",
          scaledSize: {
            width: 70,
            height: 70,
          },
        },
      });
    });
});


//Google Sign-In
window.initMap = initMap;

const decodeJwtResponse = (token) => {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
}

const handleSignIn = (jwt) => {
    console.log(jwt)
    const payload = jwt.credential
    const decoded = decodeJwtResponse(payload)
    localStorage.setItem("google_credential", JSON.stringify(decoded))
}

window.handleSignIn = handleSignIn

window.onload = () => {
    google.accounts.id.initialize({
        client_id: '167070280351-4bo5g0rolikev56n37icgj57qqetrop8.apps.googleusercontent.com',
        callback: handleSignIn
    })
    const parent = document.getElementById('google_btn')
    google.accounts.id.prompt(notification => {
        if (notification.isNotDisplayed()) {
            google.accounts.id.renderButton(parent, {theme: 'filled_blue'})
        }
    });
  const updateMapsUrl = (val) => {
    if (map) {
    }
    maps.src = `https://www.google.com/maps/embed/v1/place?key=${API_KEY}&q=${encodeURIComponent(
      val
    )}`;
  };
};