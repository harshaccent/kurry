var place;
function initMap() {
	var autocomplete = new google.maps.places.Autocomplete( $("#locsearch")[0] );
	autocomplete.addListener('place_changed', function() {
		place = autocomplete.getPlace();
	});
}

function getLocation() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(showPosition);
	} else { 
		x.innerHTML = "Geolocation is not supported by this browser.";
	}
}



function showPosition(position) {
	$.get("https://maps.googleapis.com/maps/api/geocode/json?latlng="+position.coords.latitude+","+position.coords.longitude, function(r){
		$("#locsearch").val( r["results"][0]["formatted_address"] );
	})
}


$(document).ready(function(){
	getLocation();
});
