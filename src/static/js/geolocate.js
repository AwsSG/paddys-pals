async function getLatLong(location){
	const apiURL = `http://open.mapquestapi.com/geocoding/v1/address?key=eTGQQAM5MpYGGPv0Gdrce3xvV5T7sTTU&location=${location}`;

	await fetch(apiURL).then((response) => {
		return response.json();
	}).then((data)=>{
		return processData(data.results);
	});
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
	for (let i = 0; i < results.length; i++) {
		locations.push(results[i].locations.forEach((loc) => {
			locations.push(processLocation(loc));
		}));
	}

	locations = locations.filter(el => { return el != null && el != '';});


	/**
	 * TODO: Display the locations to the user to select one
	 */
	return locations;
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

getLatLong('Dublin');
