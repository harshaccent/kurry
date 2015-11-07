var place;

function initMap() {
	var autocinput = $("#locsearch")[0];
	var autocomplete = new google.maps.places.Autocomplete(autocinput);

	google.maps.event.addDomListener(autocinput, 'keydown', function(e) {
		if (e.keyCode == 13) {
			e.preventDefault();
		}
	});

	autocomplete.addListener('place_changed', function() {
		place = autocomplete.getPlace();
		loc = place.geometry.location;
		add_hidden_inps (lookontop(autocinput, function (x) {
			return x[0].tagName == "FORM";
		}), {lat:loc.lat(), lng: loc.lng(), address: autocinput.value});
		return false;
	});
}

function getLocation() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(showPosition);
	}
}

function showPosition(position) {
	$.get("https://maps.googleapis.com/maps/api/geocode/json?latlng="+position.coords.latitude+","+position.coords.longitude, function(r){
		$("#locsearch").val( r["results"][0]["formatted_address"] );
	})
}

$(document).ready(function(){
	if(jsdata["_server"] != "gcl" )
		getLocation();
});


//$("#loginmodal").openModal();
