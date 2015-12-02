main2(js:["js/index.js", "https://maps.googleapis.com/maps/api/js?signed_in=true&libraries=drawing,places&callback=initMap"], bodystyle:{"overflow-y": "scroll"}) {
//main2(js:["js/index.js"], bodystyle:{"background-image": 'url("photo/slide1.jpg")', "background-size": "auto 100%", "background-position": "center" }) {
	header4();
	div(attr:{id: "googlemap"});
	//height(val: 300, id: "header_space");
	div(style: {"margin-top": "64px"}, class: "") {
		img(style: {width: "100%", position: "absolute"}, attr: {src: "photo/slide1.jpg"});
		div(style: {position: "relative", "top": "0px"}, class: "valign") {
			div(attr:{align: "center"}) {
				div(class: "pagecenter container") {
					div(class: "row") {
						div("class": "col l8 offset-l2 m8 s8 offset-m2 offset-s2") {
							div(class: "card-panel grey lighten-5 z-depth-1") {
								div() {
									b(color: "black", style: {"font-size": "25px"}) {
										p("Real Food");
									}
								}
								div() {
									b(color: "black", style: {"font-size": "25px"}) {
										p("Home Delivered");
									}
								}
								div(style: {"width": "20%", "border-bottom": "solid black 5px", "min-height": "2px", "margin-top": "10px", "margin-bottom": "10px"});
								div() {
									b(color: "black", style: {"font-size": "16px"}) {
										p("Fresh Ingredients, Daily Menus");
									}
								}
								div() {
									b(color: "black", style: {"font-size": "16px"}) {
										p("No Commitment, No Fuss");
									}
								}
								br();
								div() {
									b(color: "black", style: {"font-size": "25px"}) {
										p("Launching Soon!");
									}
								}
								form(attr:{"action": BASE+"menu" }){
									bigsearch(ph:"Enter Your Location", id:"locsearch", autofocus:"");
								}
							}
						}
					}
				}
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
