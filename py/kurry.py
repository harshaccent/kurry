_ec = {
	-1: "Incorrect password or OTP",
	-2: "Phone number already registered",
	-3: "OTP is Incorrect",
	-4: "Action handler not valid",
	-5: "Insufficient arguments"
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
	}
}

class kurry:
	def __init__(self):
		self.ec = None;
		self.mapping = {"login": self.login, "signup": self.signup, "sendotp": self.sendotp, "adddish": self.adddish};

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
			iid = _sql.ival("users", sifu(pkey(data, ["phone", "password", "email", "name"]), "type", typ, True));
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
