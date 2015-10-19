main(js:["js/index.js", "https://maps.googleapis.com/maps/api/js?signed_in=true&libraries=drawing,places&callback=initMap"], bodystyle:{"background-image": 'url("photo/slide1.jpg")', "background-size": "auto 100%", "background-position": "center" }) {
	header2(tablink:[HOST, "", "", "", "", "", ""], tabname:["Home", "Our Story", "Blog", "Be a Chef", "Contact Us", "Login"]);
	div() {
		div(attr:{align: "center"}) {
			div(class: "pagecenter container") {
				bigf(name: "Super Hit Meal From Super Hit Chefs", color: "white");
				height(val:40);
				bigsearch(ph:"Enter Your Location", id:"locsearch");
			}
		}
	}
}
