$( document ).ready(function(){
	$(function () {
	  $('[data-toggle="tooltip"]').tooltip()
	});
	$('.dropdown-menu').click(function(e) {
		e.stopPropagation();
	});
	runonload();
	mylib();
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
	$(".collapsible_sub").collapsible();
    $('select').material_select();
}

var page = {
	contactus:function() {
	}
};

