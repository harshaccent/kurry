import urllib

#import xlrd, requests, urllib

_agent = "gcl";

execfile("includes/setting.py");
execfile(_mslib+"py/func.py");
execfile("mslib/ocaml/run.py");

try:
	inpdata = udicttostr(json.loads(sys.argv[1]));
	_session = inpdata["session"];
	_get = inpdata["get"];
	_post = inpdata["post"];
	_urlpath = inpdata["url"]
except:
	print "Error in reading php vars";
	(_session, _get, _post, _urlpath) = ({}, {}, {}, '');


execfile(_mslib+"py/webd.py");
execfile(ROOT+"py/main.py");



print curl("http://api.textlocal.in/send/", {"username": "mohitsaini1196@gmail.com", "hash": "Mohitsaini1", "numbers": "7503759053", "sender": 'TXTLCL', "message": "Hey, This is just a message"});





# maincontent = mtmlparser();

# maincontent.readonefile("templates/test.cpp");

# print maincontent.disp() ;



#print pagehandler("index").db_init();

_sql.close_db();

#a = _sql.sval("users")
