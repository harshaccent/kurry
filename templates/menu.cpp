main2(js:["js/menu.js"], htmlstyle:{"overflow-y": "scroll"}) {
	div() {
		header4();
		div() {
			nav(class:"white", attr:{role: "container"}, style:{"border-bottom":"solid #ccc 1px"}) {
				div(class: "nav-wrapper container") {
					ul(class: "" ) {
						li() {
							a(class: "dropdown-button", attr:{"data-activates": "dropdown2", "aria-expanded": "false", "aria-haspopup": "true"}) {
								p("&nbsp;"*20+"Today, 28th Oct"+"&nbsp;"*0);
								icon(name: "arrow_drop_down", aclass:"right");
							}
						}
						li() {
							a(class: "dropdown-button", attr:{"data-activates": "dropdown3"}) {
								p("&nbsp;"*18+"All"+"&nbsp;"*0);
								icon(name: "arrow_drop_down", aclass:"right");
							}
						}
					}
				}
			}
			ul(attr:{id: "dropdown3"}, class: "dropdown-content") {
				foodtype = ["All", "Veg", "Non-Veg"];
				for(i, ii, foodtype) {
					li() {
						a(attr:{href: ""}) {
							p(i);
						}
					}
				}
			}
			ul(attr:{id: "dropdown2"}, class: "dropdown-content") {
				nextdays = ["Today, 26 Oct", "27 Oct", "28 Oct"];
				for(i, ii, day5times["timel"] ) {
					li() {
						a(attr:{href: BASE+"menu?datetime="+i}) {
							p( day5times["textl"][ii] );
						}
					}
				}
			}
		}

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
							for(i, lunch) {
								dispfood(dishinfo: i);
							}
						}
					}
					div(attr:{id: "dinner"}) {
						div(class: "row", attr:{align: "center"}) {
							for(i, dinner) {
								dispfood(dishinfo: i);
							}
						}
					}
				}
			}
		}
	}
}
