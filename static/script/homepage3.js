// const API_KEY = "AIzaSyBdPYyaT-s6ha5WXv8rEBalylzXx2iPEUk";
// let map = null;

// const initMap = () => {
//   const sf = { lat: 37.7606508, lng: -122.4739392 };
//   // The map, centered at Uluru
//   map = new google.maps.Map(document.getElementById("map"), {
//     zoom: 13,
//     center: sf,
//     disableDefaultUI: true,
//   });
// };

// let markers = [];
// const addressButton = document.getElementById("address-button");
// const addressBox = document.getElementById("address-input");
// addressButton.addEventListener(
//   "click",
//   () => {
//     const params = new URLSearchParams({
//       address: addressBox.value,
//       citations: true,
//       meters: true,
//     });
//     fetch(`/api/parking_data?${params.toString()}`)
//       .then((r) => r.json())
//       .then((data) => {
//         console.log(data);
//         for (let citation of data.citations) {
//             markers.push(
//                 new google.maps.Marker({
//                     position: { lat: citation.lat, lng: citation.lon },
//                     title: citation.citation_location,
//                     map: map,
//                     icon: {
//                         url: '/static/images/blue-ticket.png',
//                         scaledSize: {
//                             width: 40,
//                             height: 40,
//                         },
//                     },
//                 });

//                 const infoWindow = new google.maps.InfoWindow({
//                     content: citation.citation_location,
//                 });

//                 markers.addListener("click", () =>{
//                     infoWindow.open(map, marker);
//                 });

//                 markers.push(marker);
//         });

//         const meter = new google.maps.Marker({
//             position: { lat: data.min_meter.lat, lng: data.min_meter.lon },
//             title: data.min_meter.street_id + data.min_meter.street_name,
//             map: map,
//             icon: {
//                 url: '/static/images/red-meter-marker.png',
//                 scaledSize: {
//                     width: 40,
//                     height: 40,
//                 },
//             }
//         }); 
//             const infoWindow = new google.maps.InfoWindow({
//                 content: data.min_meter.street_id + data.min_meter.street_name,
//             });

//         meter.addListener('click', () => {
//             infoWindow.open(map, meter);
//             // draw box
//         });

//         markers.push(meter);

//         new google.maps.Marker({
//             position: { lat: data.search_coords.lat, lon: data.search_coords.lon },
//             title: data.search_coords.lat + data.search_coords.lon,
//             map: map,
//             icon: {
//                 url: '/static/images/user.png',
//                 scaledSize: {
//                     width: 40,
//                     height: 40,

//         }

//                 },
//             }),
//         }),  
//     }); 
    






// // for (const marker of markers) {
// //     const markerInfo = `
// //         <h1>${marker.title}</h1>
// //         <p>
// //             Ticket written at: <code>${marker.position.lat()}</code>
// //             <code>${marker.position.lng()}</code>
// //         </p>
// //     `;
    
// //     const infoWindow = new google.maps.InfoWindow({
// //         content: markerInfo,
// //         maxWidth: 200,
// //     });

// //     marker.addListener('click', () => {
// //         infoWindow.open(basicMap, marker);
// //     });
// //   }
//   //
// //;
// // The marker, positioned at Uluru
// // const marker = new google.maps.Marker({
// //   position: sf,
// //   map: map,
// // });
// // }

// //function searchClicked() {
// /*
//         In your HTML file:
//         <input type="text" id="lat-input"/>
//         <input type="text" id="long-input"/>
//     */
// // Look up the lat-input element, then find what the user has typed into it
// //const lat_value = document.getElementById("lat-input").value;
// //const long_value = document.getElementById("long-input").value;
// // const address = document.getElementById("address-input").value;
// // fetch(`/api/parking_data?lat=${lat}&lon=${lon}`)
// //     .then(response => response.json())
// //     .then(meters => {
// //         console.log(meters);
// //         const mapped = meters.map(m => new google.maps.Marker({
// //             position: {
// //                 lat: m.lat,
// //                 lng: m.lon
// //             },
// //             map
// //         }));
// //    });
// //}

// window.initMap = initMap;

// const decodeJwtResponse = (token) => {
//     var base64Url = token.split('.')[1];
//     var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
//     var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
//         return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
//     }).join(''));

//     return JSON.parse(jsonPayload);
// }

// const handleSignIn = (jwt) => {
//     console.log(jwt)
//     const payload = jwt.credential
//     const decoded = decodeJwtResponse(payload)
//     localStorage.setItem("google_credential", JSON.stringify(decoded))
// }

// window.handleSignIn = handleSignIn

// window.onload = () => {
//     google.accounts.id.initialize({
//         client_id: '167070280351-4bo5g0rolikev56n37icgj57qqetrop8.apps.googleusercontent.com',
//         callback: handleSignIn
//     })
//     const parent = document.getElementById('google_btn')
//     google.accounts.id.prompt(notification => {
//         if (notification.isNotDisplayed()) {
//             google.accounts.id.renderButton(parent, {theme: 'filled_blue'})
//         }
//     });
//   const updateMapsUrl = (val) => {
//     if (map) {
//     }
//     maps.src = `https://www.google.com/maps/embed/v1/place?key=${API_KEY}&q=${encodeURIComponent(
//       val
//     )}`;
//   };
// };
