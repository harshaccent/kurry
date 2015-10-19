var map = null;
function initMap() {
	var myCenter = new google.maps.LatLng( 28.6667, 77.1923144 );
	map = new google.maps.Map(document.getElementById('map'), {
		center: {lat: 28.6667, lng: 67.9663144},
		zoom: 12,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	});
	$.get("http://ip-api.com/json", function(data){
		map.setCenter({'lat':data.lat, 'lng':data.lon});
	});
	var marker=new google.maps.Marker({
		position: myCenter,
		icon: "photo/curloc1.png"
	});
	marker.setMap(map);
}

