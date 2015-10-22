
def msgdummy(phone, msg):
	msgfile = "data/msgf";
	writefd(open(msgfile, "a"), "To: {0}\nAt: {1}\n{2}\n{3}\n{4}\n{4}\n\n\n".format(phone, t2f_time(), '-'*20, msg, '-'*20));

def maildummy(email, sub, msg):
	mailfile = "data/mailf";
	writefd(open(mailfile, "a"), "To: {0}\nSubject: {1}\nAt: {2}\n{3}\n{4}\n{5}\n{5}\n\n\n".format(email, sub, t2f_time(), '-'*20, msg, '-'*20));

def msgreal(phone, msg):
	pass

def mailreal(email, sub, msg):
	pass
	
def sendmsg(phone, msg):
	 msgreal(phone, msg) if _config["realmsg"] else msgdummy(phone, msg);

def sendmail(email, sub, msg):
	 mailreal(email, sub, msg) if _config["realmail"] else maildummy(email, sub, msg);

def filemsg(phone, fn, data={}):
	sendmsg(phone, read_file(fn).format(**data));

def filemail(email, fn, data={}):
	msg = read_file(fn).format(**data);
	sendmail(email, msg.split("\n")[0], msg.split("\n", 1)[1]);

def init_mailmsgsystem():
	elc("mkdir -p data; > data/msgf; > data/mailf; chmod 777 data -R ");

def login(id, typ):
	global _session;
	_session["login"] = {"id": id, "type": typ};

def islogin():#Also return login type
	return _session["login"]["type"] if (g(g(_session, "login"), "id") > 0) else '';

def isloginas(t):
	if type(t) != list:
		t = [t];
	return (islogin() and (_session["login"]["type"] in t));

def logout():
	global _session;
	_session["login"] = None;

def loginid():
	if(islogin()):
		return _session["login"]["id"];
