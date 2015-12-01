main2(js:["js/index.js", "https://maps.googleapis.com/maps/api/js?signed_in=true&libraries=drawing,places&callback=initMap"], bodystyle:{"overflow-y": "scroll"}) {
//main2(js:["js/index.js"], bodystyle:{"background-image": 'url("photo/slide1.jpg")', "background-size": "auto 100%", "background-position": "center" }) {
	header4();
	div(attr:{id: "googlemap"});
	div(style: {"overflow": "visible", "height": "0px"}) {
		img(style: {width: "100%"}, attr: {src: "photo/slide1.jpg"});
	}
	div() {
		div(attr:{align: "center"}) {
			div(class: "pagecenter container") {
				bigf1(name: "Real Food", color: "black");
				br();
				bigf1(name: "Home DELIVERED", color: "white", font: "60px");
				br();
				div(style: {"width": "20%", "border-bottom": "solid black 8px", "min-height": "8px"});
				br();
				span() {
					b(color: "black", style: {"font-size": "25px"}) {
						p("Fresh Ingredients, Daily Menus");
					}
					br();
					b(color: "black", style: {"font-size": "25px"}) {
						p("No Commitment, No Fuss");
					}
				}
				br();
				form(attr:{"action": BASE+"menu" }){
					bigsearch(ph:"Enter Your Location", id:"locsearch", autofocus:"");
				}
				br();
				br();
				height(val: 500);
			}
		}
	}

	div(class: "darken-4") {
		height(val: 200);
		kurry_footer();
	}
	div(class: "modal", id: "contactusform", style: {padding: "20px"}) {
		kurry_contactus_form();
	}
	div(class: "modal", id: "aboutus", style: {padding: "20px"}) {
		kurry_aboutus();
	}
	div(class: "modal", id: "policy", style: {padding: "20px"}) {
		kurry_policy();
	}

}
