main1() {
	p(_session);
	form(attr: {enctype: "multipart/form-data", method: "post"}) {
		input(attr: {type: "file", name:"mohit"});
		button(attr: {type: "submit"}) {
			p("Submit");
		}
		table1(thead: thead, rows: rows, class: "bordered");
	}
}
