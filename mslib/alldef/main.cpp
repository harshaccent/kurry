define main(acss:["css/materialize.min.css", "css/lib.css", 'css/materialize.min.css', 'css/custom-stylesheet.css', 'css/jquery.bxslider.css', 'https://fonts.googleapis.com/icon?family=Material+Icons', 'css/lib.css', 'css/main.css', 'css/style.css'], ajs:['mslib/js/jquery-2.1.1.min.js','mslib/js/materialize.min.js','mslib/js/jquery.bxslider.min.js','mslib/js/jquery.easing.1.3.js','mslib/js/jquery.raty.js','mslib/js/lib.js','mslib/js/mohit.js','mslib/js/mohitlib.js','mslib/js/main.js'], title: "Class Pundit", css:[], js:[], bodystyle:{}) {
	css = acss + css;
	js = ajs + js;
	p("<!DOCTYPE html>");
	html(){
		head(){
			base(attr:{href:HOST});
			title(){ p(title); }
			for(i, css) {
				link(attr:{href:i, rel:"stylesheet", type:"text/css"});
			}
		}
		body(style:bodystyle){
			innerHTML();
			for(i, js) {
				script(attr:{type:"text/javascript", src:i});
			}
		}
	}
}


define disptabs(tabname: [], tablink: []) {
	for(i, j, tabname) {
		li() {
			a(attr: { href: tablink[j] } ) {
				p(i);
			}
		}
	}
}

define header1(tabname:[], tablink:[]) {
	div(class: "navbar-fixed ") {
		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: BASE}, class: "brand-logo") {
					img(attr:{src: "photo/mylogo1.png"}, class: "circle responsive-img", style:{"vertical-align": "middle"});
				}
				form(class: "right") {
					div(class: "input-field lighten-1") {
						input(attr:{type:"search", placeholder:"Search"}, color: "black");
						label(attr:{"for":"search"}, class: "") {
							i(class: "mdi-action-search");
						}
						i(class: "mdi-navigation-close");
					}
				}

				ul(class: "right hide-on-med-and-down") {
					disptabs(tabname: tabname, tablink: tablink);
				}
			}
		}
	}
}

define header2(tabname:[], tablink:[]) {
	div(class: "navbar-fixed ") {
		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: BASE}, class: "brand-logo") {
					img(attr:{src: "photo/mylogo1.png"}, class: "circle responsive-img", style:{"vertical-align": "middle"});
				}
				ul(class: "right hide-on-med-and-down" ) {
					disptabs(tabname: tabname, tablink: tablink);
				}
			}
		}
	}
}


define icon(aclass: "") {
	i(class: "material-icons "+aclass){
		p(name);
	}
}

define icon1() {
	img(attr:{src: img}, style:{"margin-bottom": "-5px"});
}


define checkbox1(checked: None, label:"Check", aclass:"") {
	span() {
		input(attr:{type: "checkbox", id: id, checked: checked}, class: "filled-in "+aclass, onclick: onclick);
		label(attr:{"for": id}) {
			p(label);
		}
	}
}


define bigf(font: "65px") {
	span(style:{"font-size": font, "text-shadow": "3px 3px 3px #000, 2px 2px 2px blue"}, color: color) {
		p(name);
	}
}


define height() {
	div(style:{height: val+"px"});
}
