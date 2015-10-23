_sql = sqllib();
execfile(ROOT+"py/kurry.py");
_kurry = kurry();

_config["users"] = {"a": "Admin", "c": "Chef", "u": "User"};

_config["adminpass"] = "Admin_Secure432";

class pagehandler:
	def __init__(self, name):
		self.name = name;
		if(False and _server == "gcl"):
			elc("python client.py 10.208.20.186 ./compile");
		self.jsdata = {"HOST": HOST, "BASE": BASE, "curpage": self.name, "_server": _server, "_ec": _ec };
		self.methodmap = {"index": self.index, "test": self.test, "account": self.account, "profile": self.profile};

	def call(self):
		runmethod = (rifn(self.methodmap[self.name](), {}) if self.methodmap.has_key(self.name) else {});
		logininfo = { "islogin": islogin(), "loginid": loginid() };
		mifu(self.jsdata, logininfo);
		return mifu(sifu(runmethod, "jsdata", json.dumps(self.jsdata)), logininfo);

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
			for i in ["users", "chef"]:
				print _sql.q("drop table if exists "+i);
		if(False):
			print _sql.q("create table if not exists users (id int NOT NULL AUTO_INCREMENT, phone varchar(100), password varchar(100), email varchar(100),  name varchar(100), address varchar(500), type varchar(3), create_time int, update_time int, last_login int, last_ip varchar(20), conf varchar(1), profilepic varchar(100), PRIMARY KEY ( id) ) ");
			print _sql.q("create table if not exists chef (chefid int, aboutus varchar(100))");
		if(False):
			print _kurry.signup({"phone": "7503759053", "password": "p"}, "a");
		if(True):
			print _sql.q("create table if not exists dishes (id int NOT NULL AUTO_INCREMENT, cid int, price int, title varchar(100), descp varchar(1000), pic varchar(200), PRIMARY KEY ( id) )");



	def test(self):
		mprint(_session);
		try:
			mprint( _files );
			_toresize[_files["mohit"]["tmp_name"]] = ["data/files/mohit.jpg", 100, 97];
		except:
			mprint("Problem Occured");
		pass


	def account(self):
		if(islogin() == "a"):
			allu = _sql.sval("users");
			users = list(pkey1(mapp(lambda x,y: _config["users"][x] if  y=="type" else x , i), ["id", "name", "phone", "email", "type"]).values()  for i in allu);
			return {"users": {"rows": users, "thead": ["UserID", "Name", "Phone", "Email", "User Type"] } };
		else:
			redirect(HOST);


	def profile(self):
#		mprint(_post, _files);
		if(has_key(_post, "adddish")):
			_post["action"] = "adddish";
			_kurry.handler(_post, _actions[_post["action"]]);
		uid = g(_get, "uid", loginid())
		uinfo = _sql.sval("users", "*", {"id": uid}, 1);
		rdata = {};
		if(uinfo):
			viewtype = "guest";
			if(uinfo["type"] == "c"):
				rdata["day5times"] = _kurry.day5times();
				if(isloginas("a")):
					viewtype = "a";
					pass
				elif( isloginas("c") and uid == loginid() ):
					viewtype = "self";
					pass
				else:
					pass
				if(viewtype == "a" or viewtype == "self"):
					rdata["dishdata"] = _sql.g("select users.name, users.profilepic, dishes.* from dishes left join users on users.id = dishes.cid AND cid={cid}", {"cid": uid});
			elif(uinfo["type"] == "u"):
				pass
			return mifu(rdata, {"uid": uid, "uinfo": uinfo, "viewtype": viewtype});
		else:
			redirect(HOST);






