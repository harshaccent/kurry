

mergeforce(funcs, {
	addfav: function() {
		runf("error", {msg: "You need to login first !"});
	},
	slideform: function () {
		$(obj).parent().find("form").slideToggle();
	}
});


ms.showtextarea = function(obj) {
	$(obj).parent().find("div.edittext").slideDown();
}

