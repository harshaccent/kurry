main1(js:["js/index.js", "https://maps.googleapis.com/maps/api/js?signed_in=true&libraries=drawing,places&callback=initMap"], bodystyle:{"background-image": 'url("photo/slide1.jpg")', "background-size": "auto 100%", "background-position": "center" }) {
	header4();
	div(attr:{id: "googlemap"});
	div() {
		div(attr:{align: "center"}) {
			div(class: "pagecenter container") {
				bigf(name: "Super Hit Meal From Super Hit Chefs", color: "white");
				height(val:40);
				form(attr:{"action": BASE+"menu" }){
					bigsearch(ph:"Enter Your Location", id:"locsearch", autofocus:"");
				}
			}
		}
	}
}
