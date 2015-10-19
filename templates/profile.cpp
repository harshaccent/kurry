main(js:["js/menu.js"], htmlstyle:{"overflow-y": "scroll"}) {
	div() {
		header2(tablink:[HOST, "", "", "", "", "", ""], tabname:["Home", "Our Story", "Blog", "Be a Chef", "Contact Us", "Login"]);
		div(class: "container-fluid") {
			div(class: "row") {
				ul(class: "tabs") {
					disptabs(liclass: "tab col s2", tabname: ["Lunch", "Dinner"], tablink: ["#lunch", "#dinner"]);
				}
			}
		}
		div(class: "container-fluid") {
			div(class: "row") {
				div(class: "col l10 offset-l1 s10 m10 offset-s1 offset-m1") {
					div(attr:{id: "lunch"}) {
						div(class: "row", attr:{align: "center"}) {
							for(i, 10) {
								dispfood() ;
							}
						}
					}
					div(attr:{id: "dinner"}) {
						div(class: "row", attr:{align: "center"}) {
							for(i, 2) {
								dispfood() ;
							}
						}
					}
				}
			}
		}
	}
}
