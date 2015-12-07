var place;

var autocinput = $("#locsearch")[0];

function add_hidden_latlng(lla) {
	add_hidden_inps (lookontop_form(autocinput), lla);
}

function initMap() {
	var autocomplete = new google.maps.places.Autocomplete(autocinput);

	google.maps.event.addDomListener(autocinput, 'keydown', function(e) {
		if (e.keyCode == 13) {
			e.preventDefault();
		}
	});

	autocomplete.addListener('place_changed', function() {
		place = autocomplete.getPlace();
		loc = place.geometry.location;
		add_hidden_latlng({lat:loc.lat(), lng: loc.lng(), address: autocinput.value});
		return false;
	});
}

function getLocation() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(showPosition);
	}
}

function showPosition(position) {
	var lat = position.coords.latitude;
	var lng = position.coords.longitude;
	$.get("https://maps.googleapis.com/maps/api/geocode/json?latlng="+lat+","+lng, function(r){
		var addrtext = r["results"][0]["formatted_address"];
		$("#locsearch").val( addrtext );
		add_hidden_latlng({lat: lat, lng: lng, address: addrtext});
	});
}

$(document).ready(function(){
	if(jsdata["_server"] != "gcl" && jsdata["_server"] != "solnki" && jsdata["_server"] != "csc")
		getLocation();
});


//$("#loginmodal").openModal();

function design_need() {
//	$("#header_space").height($($(".navbar-fixed").children()[0]).height());
}




design_need();

