main() {
	form(attr: {enctype: "multipart/form-data", method: "post"}) {
		input(attr: {type: "file", name:"mohit"});
		button(attr: {type: "submit"}) {
			p("Submit");
		}
	}
}
