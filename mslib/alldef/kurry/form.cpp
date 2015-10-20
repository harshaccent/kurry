define main1(css:[], js:[], bodystyle:{}, htmlstyle:{}) {
	js = ["js/main.js"] + js;
	main(title: "KurryBox", css: css, js:js, bodystyle:bodystyle, htmlstyle: htmlstyle) {
		innerHTML();
	}
}

define bigsearch() {
	div(class: "row", style: {"background-color":""}) {
		div(class: "col l1 m1") {
			p("&nbsp;");
		}
		div(class: "col m8 s12 l9", style:{"padding": "0px", "margin": "0px"}) {
			input(attr:{placeholder: ph, id: id, autofocus: autofocus}, class:"bigsearch definput", style:{"border-radius": "0px"});
		}
		div(class: "col m2 s12 l1 ", style:{"padding": "0px", "margin": "0px"}) {
			button(class: "bigsearchbutton waves-effect waves-light btn", style:{"border-radius": "0px"}, attr:{type:"submit"}) {
				p("Go");
				icon(name: "send", aclass: "right");
			}
		}
	}
}


define header3(tabname:[], tablink:[]) {
	div(class: "navbar-fixed ") {
		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: BASE}, class: "brand-logo") {
					img(attr:{src: "photo/mylogo1.png"}, class: "circle responsive-img", style:{"vertical-align": "middle"});
				}
				ul(class: "right hide-on-med-and-down" ) {
					li() {
						a(class: "dropdown-button", attr:{"data-activates": "dropdown2"}) {
							p("&nbsp;"*10+"Today, 28th Oct"+"&nbsp;"*10);
						}
					}
					li() {
						a(class: "dropdown-button", attr:{"data-activates": "dropdown1"}) {
							p("&nbsp;"*5+"All"+"&nbsp;"*20);
						}
					}
					disptabs(tabname: tabname, tablink: tablink);
				}
			}
		}
		ul(attr:{id: "dropdown1"}, class: "dropdown-content") {
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
			for(i, ii, nextdays) {
				li() {
					a(attr:{href: ""}) {
						p(i);
					}
				}
			}
		}
	}
}

define dispfood() {
	div(class: "col s12 l4 m6 ", style:{}) {
		div(class: " card-panel", style:{"margin-bottom":"40px", "padding":"0px"}) {
			div() {
				resimg(src: "photo/food4.jpg");
			}
			div(style: {"padding-bottom": "10px"}) {
				div(style:{padding: "10px"}) {
					div(class: "row") {
						div(class: "col l8", attr:{align: "left"}) {
							div() {
								p("Papad Ki Sabji With Halwa And palak panir");
							}
						}
						div(class: "col l4") {
							icon1(img: "photo/inr1.png");
							span(style:{"font-size": "25px", "font-weight": "600"}){
								p(100);
							}
						}
					}
					div(class: "row valign-wrapper", attr:{align: "left"}) {
						div(class: "col l2") {
							circleimg(src:"photo/chef.jpg");
						}
						div(class: "col l10"){
							div(style:{"font-weight": "500"}) {
								a1(name:"Chef Mohit Saini", href: BASE+"profile");
							}
							div() {
								starrating(val:3);
//								p("5 Start Rating.");
							}
						}
						// div(class: "col l5") {
						// 	select(class: "browser-default"){
						// 		option(){
						// 			p(1);
						// 		};
						// 		option(){
						// 			p(2);
						// 		};
						// 		option(){
						// 			p(3);
						// 		};
						// 	}
						// }
					}
				}
				// div(class: "row", style:{"padding": "12px", "padding-bottom": "0px"}) {
				// 	div(class: "col l6 grey lighten-1 left", style: {margin: "-1px"}) {
				// 		divpedding(text:"Faveroute", class: "cursp");
				// 	}
				// 	div(class: "col l6 grey lighten-1 right", style: {margin: "-1px"}) {
				// 		divpedding(text: "View", class: "cursp");
				// 	}
				// }

				div(class: "row") {
					div(class: "col l4 ") {
						button(class: "btn waves-effect waves-light btn", onclick: ["addfav"], attr:{"id": "mohit"}) {
							p("Favourite");
						}
					}
					div(class: "col l4 offset-l3") {
						button(class: "btn waves-effect waves-light btn") {
							p("Add + ");
						}
					}
//						input(attr:{type:"number", min: 0, max: 5, "value": 0});
				}


			}

		}
	}
}