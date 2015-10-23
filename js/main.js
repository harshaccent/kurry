

mergeforce(funcs, {
	addfav: function() {
		runf("error", {msg: "You need to login first !"});
	},
	slideform: function () {
		$(obj).parent().find("form").slideToggle();
	}
});
