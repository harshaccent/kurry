$( document ).ready(function(){
	$(function () {
	  $('[data-toggle="tooltip"]').tooltip()
	});
	$('.dropdown-menu').click(function(e) {
		e.stopPropagation();
	});
});


function hideshowdown(h,s){
	$("#"+h).slideUp();
	$("#"+s).slideDown();
}

function hs_toggle(ids, timetaken) {
	doforall(ids, function(e){
		$("#"+e).slideToggle(timetaken);
	});
}


var funcs={
};

function runonload(){
	$('.button-collapse').sideNav();
	$('.parallax').parallax();
	$('.materialboxed').materialbox();
	$('.slider').slider({
		full_width: true,
		height:350,
		transition:400,
		interval:3500
	});
}

var page = {
	contactus:function() {
		var myCenter = new google.maps.LatLng( 28.5453552,77.1923144 );
		function initialize() {
		  var mapCanvas = document.getElementById('map-canvas');
		  var mapOptions = {
		    center:myCenter,
		    zoom: 17,
		    mapTypeId: google.maps.MapTypeId.ROADMAP
		  }
		  var map = new google.maps.Map(mapCanvas, mapOptions);
		  var marker=new google.maps.Marker({
		    position:myCenter,
		  });
		  marker.setMap(map);
		}
		google.maps.event.addDomListener(window, 'load', initialize);
	}
};

