execfile("includes/setting.py");

_printout = ""

execfile(_mslib+"py/func.py");
execfile(_mslib+"ocaml/run.py");

_agent = "poorvi";

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


exec(read_file(ROOT+"py/main.py"));


filename = ("index" if _urlpath == "" else _urlpath);

if( filename == "ajaxactions" ):
	mprint(json.dumps(pagehandler(filename).ajaxactions()));
else:
	pageh = pagehandler(filename).call();
	maincontent = mtmlparser();
	maincontent.readcompiled(filename+".cpp");
	mprint( maincontent.disp( mifu(pageh, {"HOST": HOST, "CDN": CDN, "BASE":BASE}, True) ));

print json.dumps({"printout": _printout, "_SESSION": _session });
