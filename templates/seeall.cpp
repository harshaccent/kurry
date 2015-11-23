main1() {
	div(class: "container") {
		for(i, allt) {
			div(class: "row") {
				// div(class: "col s12 l12 m12") {
				// 	h1() {
				// 		p(i["name"]);
				// 	}
				// }
				div(class: "") {
					table1(thead: i["data"]["thead"], rows: i["data"]["rows"], class: "bordered");
				}
			}
		}
	}
}


