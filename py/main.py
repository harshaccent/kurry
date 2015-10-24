_sql = sqllib();
execfile(ROOT+"py/kurry.py");
_kurry = kurry();

_config["users"] = {"a": "Admin", "c": "Chef", "u": "User"};

_config["adminpass"] = "Admin_Secure432";

_config["realmsg"] = (_server == "aws");

class pagehandler:
	def __init__(self, name):
		self.name = name;
		if(False and _server == "gcl"):
			elc("python client.py 10.208.20.186 ./compile");
		self.jsdata = {"HOST": HOST, "BASE": BASE, "curpage": self.name, "_server": _server, "_ec": _ec };
		self.methodmap = {"index": self.index, "test": self.test, "account": self.account, "profile": self.profile, "menu": self.menu};

	def call(self):
		runmethod = (rifn(self.methodmap[self.name](), {}) if self.methodmap.has_key(self.name) else {});
		logininfo = { "islogin": islogin(), "loginid": loginid() };
		mifu(self.jsdata, logininfo);
		return mifu(sifu(runmethod, "jsdata", json.dumps(self.jsdata)), logininfo);

	def menu(self):
		daydatetime = intf(g(_get, "datetime", daystarttime()));
		outp = mapp(lambda x:_sql.g(gtable("dispdish5", 0), {"datetime": daydatetime, "lord": x}), ["l", "d"], None, lambda x: ["lunch", "dinner"][x]);
		outp["day5times"] = _kurry.day5times();
		return outp;

	def index(self):
		if(_get.has_key("logout")):
			logout();
			redirect(HOST);

	def ajaxactions(self):
		time.sleep(1);
		if( has_key(_actions, g(_post, "action"))):
			return _kurry.handler(_post,  _actions[_post["action"]]);
		else:
			return {"ec": -4};

	def db_init(self):
		if(False):
			for i in ["users", "chef", "dishes", "dispdish"]:
				# print _sql.q("drop table if exists "+i);
				print _sql.q("drop table "+i);
		if(True):
			print _sql.q("create table if not exists users (id int NOT NULL AUTO_INCREMENT, phone varchar(100), password varchar(100), email varchar(100),  name varchar(100), address varchar(500), type varchar(3), create_time int, update_time int, last_login int, last_ip varchar(20), conf varchar(1), profilepic varchar(100), profilepic_small varchar(200), PRIMARY KEY ( id) ) ");
			print _sql.q("create table if not exists chef (chefid int, aboutus varchar(100))");
		if(True):
			print _kurry.signup({"phone": "7503759053", "password": "p"}, "a");
		if(True):
			print _sql.q("create table if not exists dishes (id int NOT NULL AUTO_INCREMENT, cid int, price int, title varchar(100), descp varchar(1000), pic varchar(200), PRIMARY KEY ( id) )");
		if(True):
			print _sql.q("create table if not exists dispdish (cid int, datetime int, dishid int, lord varchar(1), plimit int, UNIQUE (cid, datetime, dishid, lord))");
		if(False):
			print _sql.q("alter table if not exists users ADD profilepic_small varchar(200)");


			
	def test(self):
		darr = dict(mapp(lambda x:daystarttime()+x*24*3600,range(5), None, lambda x: "x"+str(x)))
		rdata = {};
		day5times = _kurry.day5times();
		rdata["day5times"] = day5times;
		darr = dict(mapp(idf, day5times["timel"], None, lambda x: "x"+str(x)))
		rdata["dispdish"] = _sql.g(gtable("dispdish3", 0), {}, darr);
		rdata["dispdish1"] = _sql.g(gtable("dishes2", False), {"cid": 14});
		return mifu(sqlr2table( rdata["dispdish"]) , {"_session": _session});


	def account(self):
		if(islogin() == "a"):
			allu = _sql.sval("users");
			users = list(pkey1(mapp(lambda x,y: _config["users"][x] if  y=="type" else x , i), ["id", "name", "phone", "email", "type"]).values()  for i in allu);
			return {"users": {"rows": users, "thead": ["UserID", "Name", "Phone", "Email", "User Type"] } };
		else:
			redirect(HOST);


	def profile(self):
		uid = doifcan(lambda x:int(x), g(_get, "uid", loginid()), 0);
		if(has_key(_post, "adddish")):
			_post["action"] = "adddish";
			_kurry.handler(_post, _actions[_post["action"]]);
		if(has_key(_files, "profilepic")):
			nname = uploadimg(_files["profilepic"]["tmp_name"], _files["profilepic"]["name"], [307, 307]);
			_sql.uval("users", {"profilepic": nname}, {"id": uid}, 1);
		uinfo = _sql.sval(gtable("users1"), "*", {"id": uid}, 1);
		rdata = {};
		if(uinfo):
			viewtype = "guest";
			canedit = False;
			if(uinfo["type"] == "c"):
				uinfo["aboutus"] = str(uinfo["aboutus"]);
				if(isloginas("a")):
					viewtype = "a";
					canedit = True;
					pass
				elif( isloginas("c") and uid == loginid() ):
					viewtype = "self";
					canedit = True;
					pass
				else:
					pass
				day5times = _kurry.day5times();
				rdata["day5times"] = day5times;
				#rdata["dishdata1"] = _sql.g(gtable("dishes2", False), {"cid": uid});
				darr = dict(mapp(idf, day5times["timel"], None, lambda x: "x"+str(x)))
				rdata["dispdata"] = _sql.g("select * from "+gtable("dispdish3")+" where cid={cid}", {"cid": uid}, darr);
			elif(uinfo["type"] == "u"):
				pass
			return mifu(rdata, {"uid": uid, "uinfo": uinfo, "viewtype": viewtype, "canedit": canedit});
		else:
			redirect(HOST);






