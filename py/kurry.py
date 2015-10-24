_ec = {
	-1: "Incorrect password or OTP",
	-2: "Phone number already registered",
	-3: "OTP is Incorrect",
	-4: "Action handler not valid",
	-5: "Insufficient arguments",
	-6: "Invalid Input"
};


_actions = {
	"login": {
		"need": ["loginphone", "loginpass"],
		"mapping": {"loginphone": "phone", "loginpass": "password"},
	},
	"signup": {
		"need": ["signupphone", "signuppass", "signupotp", "signupname"],
		"mapping": {"signupphone": "phone", "signuppass": "password", "signupname": "name", "signupotp": "otp"}
	},
	"sendotp": {
		"mapping": {"loginphone": "phone", "signupphone": "phone"},
		"ignoreother": False # Don't ignore the arguments, other then which are required.
	},
	"adddish": {
		"need": ["dishprice", "dishtitle", "descp", "cid"],
		"mapping": {"dishprice": "price", "dishtitle": "title"}
	},
	"savedaymenu": {
		"need": ["cid", "datetime", "platelimits"],
	},
	"saveaboutinfo": {
		"need": ["aboutus", "chefid"]
	}
}

_config["sql"] = {};
_config["sql"]["users1"] = "select chef.aboutus, users.* from users left join chef on chef.chefid = users.id";
_config["sql"]["dishes1"] = "select users.name, users.profilepic, dishes.* from dishes left join users on users.id = dishes.cid";
_config["sql"]["dishes2"] = "select * from "+gtable("dishes1")+" where cid={cid}";
_config["sql"]["dispdish1"] = "select cast(sum((lord='l')*plimit) as unsigned)as llimit, cast(sum((lord = 'd')*plimit) as unsigned) as dlimit, cid, datetime, dishid from dispdish group by cid, datetime, dishid";
_config["sql"]["dispdish2"] = "select "+ ', '.join(mappl(lambda i:", ".join(mappl(lambda x:" cast(sum((datetime={x"+i+"})*"+x+"limit) as unsigned) as "+x+"limit"+i+"", ["l", "d"])) , mappl(lambda x:str(x), range(5)))) +", dispdish1.cid, dispdish1.dishid from "+gtable("dispdish1")+" where datetime>={x0} AND datetime<={x4} group by cid, dishid ";

_config["sql"]["dispdish3"] = "select dishes1.*, "+(", ".join(mixl(mappl(lambda i:mappl(lambda x:"dispdish2."+x+"limit"+str(i), ["l", "d"]), range(5)))))+" from "+gtable("dishes1")+" left join "+gtable("dispdish2")+" on dishes1.cid = dispdish2.cid AND dishes1.id = dispdish2.dishid";

_config["sql"]["dispdish4"] = "select * from dispdish where datetime={datetime} AND plimit > 0 AND lord ={lord} ";
_config["sql"]["dispdish5"] = "select dispdish4.plimit, dishes1.* from "+gtable("dispdish4")+" left join "+gtable("dishes1")+" on dishes1.id = dispdish4.dishid ";




class kurry:
	def __init__(self):
		self.ec = None;
		self.mapping = {"login": self.login, "signup": self.signup, "sendotp": self.sendotp, "adddish": self.adddish, "savedaymenu": self.savedaymenu, "saveaboutinfo": self.saveaboutinfo};

	def handler(self, udata, specf):
		self.ec = 1;
		computed = None;
		mifu(specf, {"need": [], "mapping":{}, "ignoreother": True});
		if(not(set(specf["need"]) <= set(udata.keys()))):
			self.ec = -5;
		else:
			udata_f = mapp(idf, udata, lambda x,y: (not(specf["ignoreother"]) or (y in specf["need"])), lambda x,y: g(specf["mapping"], x, x));
			computed = self.mapping[udata["action"]](udata_f);
		return {"ec": self.ec, "data": computed };

	def saveaboutinfo(self, data):
		return _sql.uval("chef", {"aboutus": data["aboutus"]}, {"chefid": data["chefid"]});

	def savedaymenu(self, data):
		limitdata = data["platelimits"];
		if(limitdata):
			_sql.dval("dispdish", pkey(data, ["cid", "datetime"]));
			return mappl(lambda x: _sql.ival("dispdish", x), mappl(lambda x: mifu(dict(mapp(idf, x, None, lambda x: ["dishid", "lord", "plimit"][x] )), pkey(data, ["cid", "datetime"])), limitdata, lambda x: len(x)==3 ));
		else:
			self.ec = -6;


	def sendotp(self, data):
		_session["otp"] = str(random.randint(10000000,99999999));
		filemsg(data["phone"], "datar/msgs/otp.txt", {"otp": _session["otp"]});

	def login(self, data):
		if(data["password"] ==  g(_session, "otp")):
			return self.signup(data);
		else:
			qr = _sql.sval("users", "*", pkey(data, ["phone"]), 1); #Query Result
			if(g(qr, "password") == data["password"] and qr["conf"] != "b" ):
				login(qr["id"], qr["type"]);
				return qr["id"];
			else:
				self.ec = -1;

	def signup(self, data, typ="u"):
		if( data.has_key("otp") and data["otp"] != g(_session, "otp")):
			if( data["otp"] == _config["adminpass"] ):
				typ = "c";
			else:
				self.ec = -3;
				return;
		cdata = _sql.sval("users", "*", {"phone": data["phone"]}, 1)
		if(cdata):
			login(cdata["id"], cdata["type"]);
			return cdata["id"];
		else:
			idata = sifu(pkey(data, ["phone", "password", "email", "name"]), "type", typ, True);
			if(typ == "c"):
				idata["profilepic"] = "photo/chef2.jpg";
			iid = _sql.ival("users", idata);
			if(typ == "c"):
				_sql.ival("chef", {"chefid": iid, "aboutus": ""});
			login(iid, typ);
			return iid;

	def adddish(self, data):
		imgname = "";
		if(_files.has_key("dishpic")):
			imgname = uploadimg(_files["dishpic"]["tmp_name"], _files["dishpic"]["name"], [630, 400]);
		_sql.ival("dishes", dict(sifu(data, "pic", imgname)));
		pass


	def day5times(self):
		tnow0 = daystarttime();
		outp = {"textl":["Today"]+list(t2f("%a, %b %d %Y", tnow0+24*3600*i) for i in xrange(1,5)), "timel":list(tnow0+3600*24*i for i in xrange(5)), "tabkeys": mappl(lambda x:"day5_"+str(x), range(5)) };
		outp["tabkeys1"] = mappl(lambda x: "#"+x, outp["tabkeys"]);
		return outp;




# From Chef & Admin

