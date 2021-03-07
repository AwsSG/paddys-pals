let drawMap = document.getElementById("map");










// -------------- FORM CONTROLS ----------------------

const input = document.querySelectorAll("input");
const textArea = document.querySelector("textarea");
const submit = document.querySelector("#submit-form");

submit.addEventListener("click", () => {
    input.forEach(element => element.value = "");
    textArea.value = "";
});

// --------------- GEOCODING -------------------------

// function getLatLng(location, cb) {
//     let partyLocation = location;
//     const apiURL = `http://open.mapquestapi.com/geocoding/v1/address?key=eTGQQAM5MpYGGPv0Gdrce3xvV5T7sTTU&location=${partyLocation}`;
//     let apiReturn;

//     let xhr = new XMLHttpRequest();

//     xhr.open("GET", apiURL);
//     xhr.send();

//     xhr.onreadystatechange = function() {
//         if(this.readyState == 4 && this.status == 200) {
//             cb(JSON.parse(this.responseText));
//         }
//     };
// };

// function apiData(jsonData) {
//     apiReturn = jsonData.results[0].locations[0].latLng;
//     // console.log(apiReturn);
//     return apiReturn;
// }


// let latLng = getLatLng("Dublin, Ireland", apiData);
// console.log(latLng);

async function getData() {
    let apiData = {
        url: "http://open.mapquestapi.com/geocoding/v1/address?key=eTGQQAM5MpYGGPv0Gdrce3xvV5T7sTTU&location=",
        partylocation: "Dublin, Ireland"
    }
    let apimapURL = apiData.url + apiData.partylocation;

    const response = await fetch(apimapURL);
    const coords = await response.json();

    return coords;

}



function getLatLng(async () => {
    let coords;

    try {
        coords = await getData();
    } catch (e) {
        console.log("Error!");
        console.log(e);
    }

    console.log(coords);
})

getLatLng();