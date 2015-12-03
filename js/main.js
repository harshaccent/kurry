

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



(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-50390872-2', 'auto');
ga('send', 'pageview');

