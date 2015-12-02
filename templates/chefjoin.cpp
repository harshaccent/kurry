chefjoinjs = ["js/chefjoin.js"];

if(true) {
	chefjoinjs = chefjoinjs + ["https://maps.googleapis.com/maps/api/js?signed_in=true&libraries=drawing,places&callback=initMap"];
}

main2(js: chefjoinjs) {
	header4();
	div() {
		div(class: "container") {
			height(val: 100);
			form(data:{onsubmit: "sreq", bobj: "", action: "chefjoinus", restext: "Submitted", errorh: "error_login"}, attr:{id: "mohit"}) {
				errorbox();
				div(class: "row"){
					input1(label: "Name", id: "name");
					input1(label: "Mobile number", id: "mobile", dc: "phone");
					input1(label: "Email Id", id: "email", dc: "email");
					input1(label: "Address", id: "gaddress", attr:{onkeydown: "return notenterkey(event);"});
					input1(label: "Extra Address [Building Number]", id: "address", aclass: "col l12 m12 s12");
					select2(tlist: ["Male", "Female"], vlist: ["M", "F"], toptext: "Gender", name: "gender");
					select2(tlist: config["chefagelist"], toptext: "Age", name: "age");
					select2(tlist: config["chefhowmanypeople"], toptext: "For How many you can cook", name: "cookpeople");
					mselect2(id: "languages", tlist: config["cheflanguages"], label: "Select languages", selectall: "Select All");
				}
				div(class: "row"){
					switch2(label: "Do you Cook NonVeg Food", name: "isnonveg");
					switch2(label: "Do you have academic degree in cooking ?", class: "col l6", name: "isdegree");
				}
				div(class: "row") {
					textarea1(label: "Ten Dishes, you would like to have", class: "materialize-textarea", id: "dishes");
				}
				div() {
					button1(name: "Submit", attr:{type: "submit"});
				}
			}
		}
	}
}
