main2(js:["js/cart.js"], htmlstyle:{"overflow-y": "scroll"}) {
	div() {
		header4();
		div(class: "container") {
			div(class: "row") {
				textdiv(name: "My Cart", class: "bigtext");
			}
			div(class: "row") {
				table(class: "bordered") {
					thead() {
						for(i, ["delivery Date", "Chef", "", "Dish", "Price", "No. of plates", "Delivery Slot", "Status"]) {
							th() {
								p(i);
							}
						}
					}
					tbody() {
						for(i, ii, cartl) {
							tr(class: "cartitems", datas:{ datetime: i["datetime"], cid: i["cid"], lord: i["lord"], dishid: i["dishid"]}) {
								td() {
									p(i["datetimetext"]);
								}
								td() {
									profilea1(name: i["name"], uid: i["cid"]);
								}
								td() {
									p({"l": "Lunch", "d": "Dinner"}[i["lord"]]);
								}
								td() {
									p(i["title"]);
								}
								td() {
									icon1(img: "photo/inr2.png");
									span(class: "itemprice") {
										p(i["price"]);
									}
								}
								td() {
									select1(tlist: i["tlist"], aclass: "numitem", attr:{onchange: "settotalprice();"});
								}
								td() {
									select1(tlist: dslots[i["lord"]], aclass: "dslots");
								}
								td() {
									div(style: {color: "red"}, data:{iserror: (i["error"] != "")}) {
										p(i["error"]);
									}
								}
								td() {
									button1(name: "Delete", data: {onclick: "sreq", action: "delfromcart", restext: "Deleted", res: "removerow(obj);"}, datas: {id: i["id"] });
								}
							}
						}
					}
				}
			}
			div(class: "row") {
				div(class: "col l12") {
					span(style: {"font-size": "25px"}) {
						p("Total Price: ");
						span(id: "totalprice") {
							p(100);
						}
						icon1(img: "photo/inr1.png");
					}
				}
				div(class: "col l12") {
					span(style: {"font-size": "18px"}) {
						p("Address: ");
						span() {
							p(address[2]);
						}
					}
					a1(name: "change", href:"", style: {"font-size": "11px"});
				}
				form(data: {action: "order", onsubmit: "order", bobj: "", restext: "Ordered"}) {
					input1(label: "Extra Address", id: "eaddress");
					div(class: "col l12") {
						button1(name: "Order", attr:{type: "submit"});
					}
				}
			}
		}
		div(class: "dnone") {
			textdiv(id: "lat", name: address[0]);
			textdiv(id: "lng", name: address[1]);
		}
	}
}
