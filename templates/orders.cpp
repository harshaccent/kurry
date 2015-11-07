main2(js:["js/cart.js"], htmlstyle:{"overflow-y": "scroll"}) {
	div() {
		header4();
		div(class: "container") {
			div(class: "row") {
				textdiv(name: "Orders", class: "bigtext");
			}
			div(class: "row") {
				table(class: "bordered") {
					thead() {
						for(i, ["Odered At", "Delivery Date", "Chef", "User", "Dish", "Price", "Chef Address", "User Address", "Status"]) {
							th() {
								p(i);
							}
						}
					}
					tbody() {
						for(i, ii, orderl) {
							tr(class: "cartitems", datas:{ datetime: i["datetime"], cid: i["cid"], lord: i["lord"], dishid: i["dishid"]}) {
								td() {
									p(i["timetext"]);
								}
								td() {
									p(i["datetimetext"]);
								}
								td() {
									profilea1(name: i["cname"], uid: i["cid"]);
								}
								td() {
									profilea1(name: i["uname"], uid: i["uid"]);
								}
								td() {
									p(i["title"]);
								}
								td() {
									icon1(img: "photo/inr2.png");
									span(class: "itemprice") {
										p(i["price"]+'*'+i["numplate"]+"="+(i["price"]*i["numplate"]));
									}
								}
								td() {
									p("("+i["clat"]+", "+i["clng"]+")<br>"+i["caddress"]);
								}
								td() {
									p("("+i["lat"]+", "+i["lng"]+")<br>"+i["uaddress"]);
								}
								td() {
									p(i["status"]);
								}
							}
						}
					}
				}
			}
		}
		div(class: "dnone") {
			// textdiv(id: "lat", name: address[0]);
			// textdiv(id: "lng", name: address[1]);
		}
	}
}

