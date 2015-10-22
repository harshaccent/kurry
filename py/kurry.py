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
	}
}

class kurry:
	def __init__(self):
		self.ec = None;
		self.mapping = {"login": self.login, "signup": self.signup, "sendotp": self.sendotp};

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

	def signup(self, data):
		if( data.has_key("otp") and data["otp"] != g(_session, "otp")):
			self.ec = -3;
			return;
		cdata = _sql.sval("users", "*", {"phone": data["phone"]}, 1)
		if(cdata):
			login(cdata["id"], cdata["type"]);
			return cdata["id"];
		else:
			iid = _sql.ival("users", sifu(pkey(data, ["phone", "password", "email", "name"]), "type", "u", True));
			login(iid, "u");
			return iid;
