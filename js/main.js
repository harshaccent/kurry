

mergeforce(funcs, {
	addfav: function() {
		runf("error", {msg: "You need to login first !"});
	},
	slideform: function () {
		$(obj).parent().find("form").slideToggle();
	},
	error_login: function() {//obj, msg
		var errore = $(obj).find(".hiddenerror");
		errore.fadeIn(1000);
		errore.find(".errortext").html(msg);
	}
});


ms.showtextarea = function(obj) {
	$(obj).parent().find("div.edittext").slideDown();
}

