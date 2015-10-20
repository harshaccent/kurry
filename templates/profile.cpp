main(js:["js/menu.js"], htmlstyle:{"overflow-y": "scroll"}) {
	div() {
		header2(tablink:[HOST, "", "", "", "", "", ""], tabname:["Home", "Our Story", "Blog", "Be a Chef", "Contact Us", "Login"]);
		div(class: "container-fluid") {
			div(class: "row") {
				div(class: "col l10 offset-l1 s10 m10 offset-s1 offset-m1") {
					div(class: "row valign-wrapper") {
						div(class: "col l3", attr:{align: "center"}) {
							div() {
								circleimg(src: "photo/chef2.jpg");
							}
							div() {
								textdiv(name: "Chef Mohit Saini", font: "25px", fontw: "500");
								div(class: "row") {
									div(class: "col l6") {
										textdiv(name:38456, fontw:600);
										textdiv(name: "Dished Delivered");
									}
									div(class: "col l6") {
										textdiv(name: 56, fontw:600);
										textdiv(name: "People reviewed");
									}
								}
							}
						}
						div(class: "col l8 offset-l1") {
							textdiv(font:"25px", name:"About Mohit Saini", fontw:600);
							textdiv(font:"16px", name:"Chef Radhika Khanna is a hotel management graduate from The Institute of Tourism and Hotel Management, Salzburg. She has conceptualized restaurants like SukhoThai, Curry on the Roof & Divine. Her experience, in addition to her vast knowledge and interest in food & culture from various parts of the world, has prepared her to create Lotus Blossom, a specialty catering service providing Thai food for parties and events. Radhika wishes to revolutionize Thai food, and change the way it is perceived by foodies in the country! Chef Radhika Khanna is a hotel management graduate from The Institute of Tourism and Hotel Management, Salzburg. She has conceptualized restaurants like SukhoThai, Curry on the Roof & Divine. Her experience, in addition to her vast knowledge and interest in food & culture from various parts of the world, has prepared her to create Lotus Blossom, a specialty catering service providing Thai food for parties and events. Radhika wishes to revolutionize Thai food, and change the way it is perceived by foodies in the country!");
						}

					}
					div(class: "msdivider");
					div(attr: {align: "center"}, style:{margin:"20px"}) {
						textdiv(name: "Dishes Serving today", font: "25px");
					}
					div(class: "row", attr:{align: "center"}) {
						for(i, 10) {
							dispfood() ;
						}
					}
				}
			}
		}
	}
}
