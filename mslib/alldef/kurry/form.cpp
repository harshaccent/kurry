define main1(css:[], js:[], bodystyle:{}, htmlstyle:{}, title: "KurryBox") {
	js = ["js/main.js"] + js;
	main(title: title, css: css, js:js, bodystyle:bodystyle, htmlstyle: htmlstyle) {
		innerHTML();
//		loginmodal();
	}
}


define main2(css:[], js:[], bodystyle:{}, htmlstyle:{}, title: "KurryBox") {
	js = ["js/main.js"] + js;
	main(title: title, css: css, js:js, bodystyle:bodystyle, htmlstyle: htmlstyle) {
		innerHTML();
		loginmodal();
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

define header4() {
	if(islogin == "") {
		header2(tablink:[HOST, "", "", "", "", ""], tabname:["Home", "Our Story", "Blog", "Be a Chef", "Contact Us"]);
	} elif (islogin == "u") {
		header2_user(tablink:[HOST, "", "", "", "", ""], tabname:["Home", "Our Story", "Blog", "Be a Chef", "Contact Us"]);
	} elif (islogin == "a") {
		header2_admin(tablink:[HOST, "", "", "", "", ""], tabname:["Home", "Our Story", "Blog"]);
	} elif (islogin == "c") {
		header2_chef(tablink:[HOST, "", "", "", "", ""], tabname:["Home", "Our Story", "Blog"]);
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
//				resimg(src: "photo/food4.jpg");
				resimg(src: dishinfo["pic"]);
			}
			div(style: {"padding-bottom": "10px"}) {
				div(style:{padding: "10px"}) {
					div(class: "row") {
						div(class: "col l8", attr:{align: "left"}) {
							div() {
								p(dishinfo["title"]);
							}
						}
						div(class: "col l4") {
							icon1(img: "photo/inr1.png");
							span(style:{"font-size": "25px", "font-weight": "600"}){
								p(dishinfo["price"]);
							}
						}
					}
					div(class: "row valign-wrapper", attr:{align: "left"}) {
						div(class: "col l2") {
							circleimg(src: "photo/chef.jpg");
						}
						div(class: "col l10"){
							div(style:{"font-weight": "500"}) {
								a1(name:"Chef "+dishinfo["name"], href: BASE+"profile");
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
					if(viewtype == "a" ) {
						div(class: "col l4 ") {
							button(class: "btn waves-effect waves-light btn") {
								p("Delete");
							}
						}
						div(class: "col l4 offset-l3") {
							button(class: "btn waves-effect waves-light btn") {
								p("Edit");
							}
						}
					} elif( viewtype == "guest" ) {
						div(class: "col l4 ") {
							button(class: "btn waves-effect waves-light btn", data:{onclick: "addfav"}, attr:{"id": "mohit"}) {
								p("Favourite");
							}
						}
						div(class: "col l4 offset-l3") {
							button(class: "btn waves-effect waves-light btn") {
								p("Add + ");
							}
						}
					}
				}
			}
		}
	}
}

define l_otp_button() {
	button(class: "btn waves-effect waves-light", attr:{type: "button"}, data:{onclick: "sreq", action: "sendotp", fobj: "$(obj).parent().parent()[0]", restext: "Re-send"}) {
		p("Send OTP");
	}
}




define loginmodal() {
	div(attr:{id: "loginmodal"}, class: "modal") {
		div(class: "modal-content container-fluid") {
			div(class: "row") {
				ul(class: "tabs") {
					disptabs(liclass: "tab col l6", tablink:["#logintab", "#signuptab"], tabname:["Login", "Signup"]);
				}
			}
			div(attr:{id: "logintab"}) {
				form(data:{onsubmit:"sreq", bobj: "", action:"login", res: "ms.reload();"}) {
					div(class: "row") {
						input1(label: "Phone number", icon: "phone", aclass: "col s12 l7 m6", id:"loginphone");
						div(class: "col l4 m6") {
							l_otp_button();
						}
					}
					div(class: "row"){
						input1(label: "Password or OTP", icon: "vpn_key", aclass: "col s12 l12 m12", id: "loginpass");
					}
					div(class: "row") {
						div(class: "col") {
							button(class: "btn waves-effect waves-light", attr:{type: "submit"}) {
								p("Login");
							}
						}
					}					
				}
			}

			div(attr:{id: "signuptab"}) {
				form(data:{onsubmit:"sreq", bobj: "", action:"signup", res: "ms.reload();" }) {
					div(class: "row") {
						input1(label: "Phone number", icon: "phone", aclass: "col s12 l7 m6", id:"signupphone");
						div(class: "col l4 m6") {
							l_otp_button();
						}
					}
					div(class: "row"){
						input1(label: "Choose Password", icon: "vpn_key", aclass: "col s12 l6 m6", id: "signuppass", type:"password");
						input1(label: "OTP", icon: "vpn_key", aclass: "col s12 l6 m6", id: "signupotp");
					}
					div(class: "row"){
						input1(label: "Name", icon: "account_circle", aclass: "col s12 l12 m12", id: "signupname");
					}
					div(class: "row") {
						div(class: "col") {
							button(class: "btn waves-effect waves-light", attr:{type: "submit"}) {
								p("Signup");
							}
						}
					}
				}
			}

		}
	}
}


define table1(rows:[], thead:[]) {
	table(class: class) {
		thead() {
			for(i, thead) {
				th() {
					p(i);
				}
			}
		}
		tbody() {
			for(i, ii, rows) {
				tr() {
					for(j, jj, i) {
						td() {
							p(j);
						}
					}
				}
			}
		}
	}
}


define accont_admin() {
	div(attr:{align: "center"}) {
		height(val: 20);
		textdiv(name: "Hey Admin,\n you can login/create account of a chef using OTP as 'Admin_Secure432' ", font: "20px");
		height(val: 50);
	}
	form() {

	}
	table1(rows: usertable["rows"], thead: usertable["thead"], class: "bordered striped centered highlight");
}


define profile_chef_top1() {
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
}

define profile_chef_top2() {
	div(class: "row valign-wrapper") {
		div(class: "col l3", attr:{align: "center"}) {
			div() {
				circleimg(src: "photo/chef2.jpg");
			}
			a1(name: "Upload Profile Pic", href:"");
			div() {
				textdiv(name: "Chef "+uinfo["name"], font: "25px", fontw: "500");
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
			a1(name: "Edit");
			textdiv(font:"16px", name:"Chef Radhika Khanna is a hotel management graduate from The Institute of Tourism and Hotel Management, Salzburg. She has conceptualized restaurants like SukhoThai, Curry on the Roof & Divine. Her experience, in addition to her vast knowledge and interest in food & culture from various parts of the world, has prepared her to create Lotus Blossom, a specialty catering service providing Thai food for parties and events. Radhika wishes to revolutionize Thai food, and change the way it is perceived by foodies in the country! Chef Radhika Khanna is a hotel management graduate from The Institute of Tourism and Hotel Management, Salzburg. She has conceptualized restaurants like SukhoThai, Curry on the Roof & Divine. Her experience, in addition to her vast knowledge and interest in food & culture from various parts of the world, has prepared her to create Lotus Blossom, a specialty catering service providing Thai food for parties and events. Radhika wishes to revolutionize Thai food, and change the way it is perceived by foodies in the country!");
		}

	}
}



define profile_chef() {
	div(class: "container-fluid") {
		div(class: "row") {
			div(class: "col l10 offset-l1 s10 m10 offset-s1 offset-m1") {
				profile_chef_top1();
				div(class: "msdivider");
				div(attr: {align: "center"}, style:{margin:"20px"}) {
					textdiv(name: "Dishes Serving today", font: "25px");
				}
				div(class: "row", attr:{align: "center"}) {
					for(i, 10) {
						//dispfood() ;
					}
				}
			}
		}
	}
}


define profile_chef_self() {
	div(class: "container-fluid") {
		div(class: "row") {
			div(class: "col l10 offset-l1 s10 m10 offset-s1 offset-m1") {
				profile_chef_top2();
				div(class: "msdivider");

				div(class: "container-fluid") {
					div(class: "row") {
					}
				}
				div(class: "container-fluid") {
					div(class: "row") {
						div() {
							ul(class: "tabs") {
								disptabs(liclass: "tab col s2", tabname: ["All Dishes"]+ day5times["textl"], tablink: ["#alldishes"]+ day5times["tabkeys1"], active: day5times["tabkeys1"][0]);
							}
						}
						div(class: "col l10 offset-l1 s10 m10 offset-s1 offset-m1") {
							div(attr:{id: "alldishes"}) {
								button1(name: "Add a New Dish", data: {onclick: "slideform"});
								form(style: {display: "none"}, attr:{enctype: "multipart/form-data", method: "post"}) {
									div(class: "row") {
										input(attr:{type:"hidden", name: "cid", value: uid });
										input2(label: "Title of Dish", aclass: "col s12 l6 m6", id:"dishtitle");
										input2(label: "Price of Dish", aclass: "col s12 l6 m6", id:"dishprice");
										// input2(label: "Amount Limit", aclass: "col s12 l3 m6", id:"dishlimit");
									}
									div(class: "row"){
										textarea(class: "materialize-textarea", attr:{name: "descp", placeholder: "Dish Description"});
									}
									div(class: "row") {
										div(class: "file-field input-field") {
											div(class: "btn") {
												span() {
													p("Upload Image");
												}
												input(attr:{type:"file", name: "dishpic"});
											}
											div(class: "file-path-wrapper") {
												input(class: "file-path-validate", attr:{type: "text"});
											}
										}
									}
									div(class: "row") {
										div(class: "col") {
											button(class: "btn waves-effect waves-light", attr:{type: "submit", name:"adddish"}) {
												p("Add");
											}
										}
									}					
								}

								div(class: "row", attr:{align: "center"}) {
									for(i, dishdata) {
										dispfood(dishinfo: i) ;
									}
								}
							}
							for(i, ii, day5times["tabkeys"]) {
								div(attr:{id: i}) {
									div(class: "row", attr:{align: "center"}) {
										table(class: "bordered") {
											thead() {
												for(j, ["Title", "Price", "Add For Lunch", "Add for Dinner"]) {
													th() {
														p(j);
													}
												}
											}
											for(j, dishdata) {
												tr() {
													th() {
														p((j["title"]+"").gchars);
													}
													th() {
														p(j["price"]);
													}
												}
											}
										}
										for(j, 1+ii) {
											//dispfood() ;
										}
									}
								}
							}
						}
					}
				}

				div(attr: {align: "center"}, style:{margin:"20px"}) {
					textdiv(name: "Dishes Serving today", font: "25px");
				}
				div(class: "row", attr:{align: "center"}) {
					for(i, 0) {
						//dispfood() ;
					}
				}
			}
		}
	}
}

