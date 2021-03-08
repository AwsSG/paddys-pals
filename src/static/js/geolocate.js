async function saveParty(){
	let partyName = document.getElementById('party-name').value;
	let loc = document.getElementById('location').value;
	let startTime = document.getElementById('start-time').value;
	let finishTime = document.getElementById('finish-time').value;
	let videoLink = document.getElementById('link-conference').value;
	let partyPassword = document.getElementById('party-password').value;
	let description = document.getElementById('description').value;

	if (partyName && loc && startTime && finishTime && videoLink && partyPassword && description ){

	const apiURL = `https://open.mapquestapi.com/geocoding/v1/address?key=eTGQQAM5MpYGGPv0Gdrce3xvV5T7sTTU&location=${loc}`;
	await fetch(apiURL).then((response)=>response.json()).then((data)=>{

			let loc_data = processData(data.results);

			post_data = {
				'name': partyName,
				'longitude': loc_data.latLng.lng + "",
				'latitude': loc_data.latLng.lat + "",
				'start_time': startTime,
				'end_time' : finishTime,
				'video_link' : videoLink,
				'party_password' : partyPassword,
				'description' : description
			};
			fetch('/add_party', {
				method: 'POST',
				headers: {'content-type': 'application/json; charset=utf-8'},
				body: JSON.stringify(post_data),
			}).then((response)=>{
				console.log(response);
				window.location.reload();
			});
		});//fetch api
	} // if
}
/**
 * For each location in the results, proccess them and add them to an array
 * We can use this information to display them to the user so they can select
 * the correct option
 *
 * Returns and array of objects:
 *
 *
 * [
	 {'Country':<country>, 'County':<county>, 'City':<city>, 'latLng': <latLng>},
	 {'Country':<country>, 'County':<county>, 'City':<city>, 'latLng': <latLng>},
	 ...
   ]
 */
function processData(results){
        locations = [];
	// For each result, process each  location
	for (let i = 0; i < results.length; i++) {
		locations.push(results[i].locations.forEach((loc) => {
			locations.push(processLocation(loc));
		}));
	}

	// Filter out any empty elements
	locations = locations.filter(el => { return el != null && el != '';});


	/**
	 * TODO: Display the locations to the user to select one
	 * For now just use the first location provided, users will have to be more specific to get
	 * the result they want. Sorry users.
	 */
	if (locations.length > 0){
		return locations[0];
	}
}

/**
 * Filters out the data we want to display to the user, and gives it more
 * user friendly names than provided by the mapquestapi
 */
function processLocation(loc){
	new_loc = {}
	new_loc['Country'] = loc.adminArea1;
	new_loc['County'] = loc.adminArea4;
	new_loc['City'] = loc.adminArea5;
	new_loc['latLng'] = loc.latLng;

	//Only return the location if we have a country, county and city.
	if (new_loc['Country'] && new_loc['County'] && new_loc['City']){
		return new_loc
	}

	return
}

