
ms.getnumlimit = function(day) {
	return {"platelimits": append(mapo(function(x,y){ return [dattr(x).dishid, attr(x)["id"][0], x.value ]; }, $(".numplatelimit"), function(x){ return (x.value != "" && dattr(x)["day"] == day ); }), [0]) };
}
