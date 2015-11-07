define main1(css:[], js:[], bodystyle:{}, htmlstyle:{}, title: "KurryBox") {
	js = ["js/main.js"] + js;
	main(title: title, css: css, js:js, bodystyle:bodystyle, htmlstyle: htmlstyle) {
		innerHTML();
//		loginmodal();
	}
}


define main2(css:[], js:[], bodystyle:{}, htmlstyle:{}, title: "KurryBox") {
	js = ["js/main.js"] + js;
	main(title: title, css: css, js:js, bodystyle:bodystyle, htmlstyle: htmlstyle, acss: ["css/materialize.min.css", "css/lib.css", 'css/materialize.min.css', 'css/custom-stylesheet.css', 'css/jquery.bxslider.css', 'mslib/css/gfont.css', 'css/lib.css', 'css/main.css', 'css/style.css']) {
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
	if(islogin == None) {
		header2(tablink:[HOST, "", "", BASE+"chefjoin"], tabname:["Home", "Our Story", "Blog", "Be a Chef"]);
	} elif (islogin == "u") {
		header2_user(tablink:[HOST, "", "", BASE+"cart"], tabname:["Home", "Our Story", "Blog", "Cart"]);
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
							// circleimg(src: "photo/chef.jpg");
							circleimg(src: dishinfo["profilepic"]);
						}
						div(class: "col l10"){
							div(style:{"font-weight": "500"}) {
								profilea1(name:"Chef "+dishinfo["name"], uid: dishinfo["cid"]);
							}
							div() {
								starrating(val:3);
							}
						}
					}
				}
				div(class: "row") {
					if(islogin == "a" ) {
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
					} elif( loginid == dishinfo["cid"] ) {

					} else {
						div(class: "col l4 ") {
							button(class: "btn waves-effect waves-light btn", data:{onclick: "addfav"}, attr:{"id": "mohit"}) {
								p("Favourite");
							}
						}
						div(class: "col l4 offset-l3") {
							button(class: "btn waves-effect waves-light btn", data:{onclick: "sreq", action: "addincart", restext: "Added!"}, datas: {datetime: dishinfo["datetime"], lord: dishinfo["lord"], dishid: dishinfo["id"]}) {
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

define profilea1() {
	a1(name: name, href: BASE+"profile?uid="+uid);
}

define account_admin() {
	div(attr:{align: "center"}) {
		height(val: 20);
		textdiv(name: "Hey Admin,\n you can login/create account of a chef using OTP as 'Admin_Secure432' ", font: "20px");
		height(val: 50);
	}
	form() {

	}
	table(class: "bordered striped centered highlight") {
		thead() {
			for(i, usertable["thead"]) {
				th() {
					p(i);
				}
			}
		}
		tbody() {
			for(i, ii, usertable["rows"]) {
				tr() {
					for(j, jj, i) {
						td() {
							if((jj == 1) && (i[-1] == "Chef" )) {
								profilea1(name:j, uid: i[0]);
							} else {
								p(j);
							}
						}
					}
				}
			}
		}
	}
}


define profile_chef_top2() {
	div(class: "row valign-wrapper") {
		div(class: "col l3", attr:{align: "center"}) {
			div() {
				circleimg(src: uinfo["profilepic"]);
			}
			if(canedit) {
				form(attr:{enctype: "multipart/form-data", method: "post"}) {
					a1(name: "Upload Profile Pic", attr:{onclick: 'uploadfile(this, "profilepic");'});
				}
			}
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
			textdiv(font:"25px", name:"About "+uinfo["name"], fontw:600);
			if(canedit) {
				a1(name: "Edit", attr:{"onclick": "ms.showtextarea(this);"});
				div(class: 'edittext', style: {display: "none"}) {
					form(data: {onsubmit:"sreq", bobj: "", action:"saveaboutinfo", res: "ms.reload();"}) {
						input(attr: {type: "hidden", name: "chefid", value: uid});
						textarea(attr:{name: "aboutus"}, class: "materialize-textarea") {
							p(uinfo["aboutus"].gchars);
						}
						button1(name: "Save", attr:{type: "submit"});
					}
				}
			}
			textdiv(font:"16px", name: uinfo["aboutus"].gchars);
		}

	}
}


define profile_chef() {
	div(class: "container-fluid") {
		div(class: "row") {
			div(class: "col l10 offset-l1 s10 m10 offset-s1 offset-m1") {
				profile_chef_top2();
				div(class: "msdivider");

				div(class: "container-fluid") {
					div(class: "row") {
					}
				}
				if(canedit) {
					div(class: "container-fluid") {
						div(class: "row") {
							div() {
								ul(class: "tabs") {
									disptabs(liclass: "tab col s2", tabname: ["All Dishes"]+ day5times["textl"], tablink: ["#alldishes"]+ day5times["tabkeys1"]);
								}
							}
							div(class: "") {
								div(attr:{id: "alldishes"}) {
									height(val:20);
									if(viewtype == "a") {
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
									}

									div(class: "row", attr:{align: "center"}) {
										for(i, dispdata) {
											dispfood(dishinfo: i) ;
										}
									}
								}
								for(i, ii, day5times["tabkeys"]) {
									div(attr:{id: i}) {
										div(class: "row") {
											table(class: "bordered") {
												thead() {
													for(j, ["Title", "Price", "Add For Lunch", "Add for Dinner"]) {
														th() {
															p(j);
														}
													}
												}
												for(j, jj, dispdata) {
													tr() {
														th() {
															p((j["title"]+"").gchars);
														}
														th() {
															p(j["price"]);
														}
														th() {
															input1(label: "Plate Limit", id: "lunch_"+jj+"_"+ii, data:{dishid: j["id"], day:ii}, iclass: "numplatelimit", value: j["llimit"+ii]);
														}
														th() {
															input1(label: "Plate Limit", id: "dinner_"+jj+"_"+ii, data:{dishid: j["id"], day: ii}, iclass: "numplatelimit", value: j["dlimit"+ii]);
														}
													}
												}
											}
											div() {
												if(dispdata.len != 0) {
													button1(name: "Save", data:{action: "savedaymenu", "onclick": "sreq", params: "ms.getnumlimit("+ii+")"}, datas:{datetime: day5times["timel"][ii], cid: uid});
												}
											}
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
					for(i, dispdata) {
						if( (i["llimit0"] > 0) || (i["dlimit0"] > 0) ) {
							dispfood(dishinfo: i) ;
						}
					}
				}
			}
		}
	}
}


define select1(tlist:[], class: "browser-default", aclass: "") {//class, tlist, vlist, toptext, selected
	select(class: class+" "+aclass, name: name, attr:attr) {
		if(toptext != None) {
			option(attr:{value: ""}) {
				p(toptext);
			}
		}
		for(i, ii, tlist) {
			attrs = {};
			if (vlist != None) {
				attrs["value"] = vlist[ii];
			} else {
				attrs["value"] = (ii+1);
			}
			if( selected == ii ) {
				attrs["selected"] = "";
			}
			option(attr:attrs) {
				p(i);
			}
		}
	}
}

define select2(tlist:[], dclass: "col l3 s12 m6", class: "browser-default") {
	div(class: dclass) {
		select1(class: class, tlist: tlist, vlist: vlist, toptext: toptext, selected: selected);
	}
}

define mselect(tlist:[]) {
	for(i, ii, tlist) {
		attrs = {};
		if (vlist != None) {
			attrs["value"] = vlist[ii];
		} else {
			attrs["value"] = (ii+1);
		}
		if( selected == ii ) {
			attrs["selected"] = "";
		}
		checkbox1(label: i, id: id+"_"+ii);
	}
}


define mselect1(tlist:[]) {
	div(id: id, class: "dropdown-content p5", tlist:[]) {
		mselect(vlist:vlist, tlist: tlist, id: id);
	}
	a(class: "dropdown-button", data:{activates: id}) {
		p(label);
	}
}

define mselect2(class: "col l3 s12 m6") {
	div(class: class) {
		div(class: "mselect complexinput", data:{complexinput: "ci_checkbox"}, attr: {name: id}) {
			mselect1(id: id, tlist: tlist, label: label, selectall: selectall);
		}
	}
}


define switch1(on: "Yes", off: "No") {
	div(class: "switch") {
		label() {
			p(off);
			input(attr:{type: "checkbox", name: name});
			span(class: "lever");
			p(on);
		}
	}
}


define switch2(class: "col l3 s12 m6") {
	div(class: class) {
		div(class: "m5") {
			p(label);
			switch1(name: name);
		}
	}
}

