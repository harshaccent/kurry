execfile("includes/setting.py");

_printout = ""
try:
	(_session, _get, _post, _urlpath) = tuple( list(json.loads(sys.argv[i]) for i in range(1,4))+ [sys.argv[4]] );
except:
	(_session, _get, _post, _urlpath) = tuple([{}]*3+['']);

_urlpath = _urlpath[1:];
_localtz = pytz.timezone("Asia/Calcutta");

execfile(_mslib+"py/func.py");
execfile(_mslib+"ocaml/run.py");
execfile(ROOT+"py/main.py");

filename = ("index" if _urlpath == "" else _urlpath);

pageh = pagehandler(filename).call();


maincontent = mtmlparser();

maincontent.readcompiled(filename+".cpp");

mprint( maincontent.disp( mifu(pageh, {"HOST": HOST, "CDN": CDN, "BASE":BASE}, True) ));

mprint(_urlpath);

print json.dumps({"printout": _printout, "_SESSION": _session });

