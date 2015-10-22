_sql = sqllib();
execfile(ROOT+"py/kurry.py");
_kurry = kurry();



class pagehandler:
	def __init__(self, name):
		self.name = name;
		if(False and _server == "gcl"):
			elc("python client.py 10.208.20.186 ./compile");
		self.jsdata = {"HOST": HOST, "BASE": BASE, "curpage": self.name, "_server": _server, "_ec": _ec };
		self.methodmap = {"index": self.index, "test": self.test};

	def call(self):
		runmethod = (rifn(self.methodmap[self.name](), {}) if self.methodmap.has_key(self.name) else {});
		logininfo = { "islogin": islogin(), "loginid": loginid() };
		mifu(self.jsdata, logininfo);
		return mifu(sifu(runmethod, "jsdata", json.dumps(self.jsdata)), logininfo);

	def index(self):
		if(_get.has_key("logout")):
			logout();

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

	def test(self):
		return {"otp": _session["otp"], "_session": _session};



