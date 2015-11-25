main2(js:["js/index.js", "https://maps.googleapis.com/maps/api/js?signed_in=true&libraries=drawing,places&callback=initMap"], bodystyle:{"background-image": 'url("photo/slide1.jpg")', "background-size": "auto 100%", "background-position": "center" }) {
//main2(js:["js/index.js"], bodystyle:{"background-image": 'url("photo/slide1.jpg")', "background-size": "auto 100%", "background-position": "center" }) {
	header4();
	div(attr:{id: "googlemap"});
	div() {
		div(attr:{align: "center"}) {
			div(class: "pagecenter container") {
				// bigf(name: "Super Hit Meal From Super Hit Chefs", color: "white");
				bigf1(name: "Real Food Home Delivered", color: "white");
				br();
				bigf1(name: "-----------------------------------", color: "white");
				br();
				bigf1(name: "Fresh Ingredients, Daily Menus ", color: "white");
				br();
				bigf1(name: "No Commitment, No Fuss", color: "white");
				form(attr:{"action": BASE+"menu" }){
					bigsearch(ph:"Enter Your Location", id:"locsearch", autofocus:"");
				}
			}
		}
	}
	div(class: "indexpage_footer white darken-4") {
		kurry_footer();
	}
}
