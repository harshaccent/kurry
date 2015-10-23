main1(js:["js/menu.js"], htmlstyle:{"overflow-y": "scroll"}) {
	div() {
		header4();
		if( (viewtype == "self") || (viewtype == "a")) {
			profile_chef_self();
		} else {
			profile_chef();
		}
	}
}
