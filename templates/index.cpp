main(js:["js/index.js", "https://maps.googleapis.com/maps/api/js?signed_in=true&libraries=drawing&callback=initMap"]) {
	header1(tablink:[HOST, "", ""], tabname:["Home", "Our Story", "Contact Us"]);
	div(attr:{id: "map"}, style: {height: "100%"});
	div(class: "catgselect") {
		ul(class: "collapsible", attr:{"data-collapsible": "accordion"}) {
			for(i, ii, catg) {
				li() {
					div(class: "collapsible-header") {
						icon1(img: i["icon"]);
						// icon(name: "filter_drama");
						p(i["name"]);
					}
					div(class: "collapsible-body") {
						div(class: "subcats1", style:{padding: "5px", "padding-left":"20px", "padding-bottom":"0px", "padding-top": "0px" }) {
							ul(class: "collapsible_sub", attr:{"data-collapsible": "accordion"}) {
								for(j, jj, i["child"]) {
									li(class: "") {
										div(class: "collapsible-header", style:{"border-bottom": "solid black 0px", "border-top": "1px solid #DDD"}) {
											p(j["name"]);
											// checkbox1(label: j["name"], id: "catsubcat"+ii+"_"+jj);
										}
										div(class: "collapsible-body") {
											div(class: "subcats2", style:{"padding-left": "30px"}) {
												ul() {
													li() {
														div() {
															checkbox1(label: "Select All", id: "catsubcat"+ii+"_"+jj+"_"+"selectall", aclass:"selectall", onclick:["selectall"]);
														}
													}
													for(k, kk, j["child"].len) {
														li() {
															div() {
																checkbox1(label: j["child"][k], id: "catsubcat"+ii+"_"+jj+"_"+kk);
															}
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
}

