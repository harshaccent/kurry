execfile("includes/setting.py");
execfile(_mslib+"py/func.py");
execfile("mslib/ocaml/run.py");
execfile(ROOT+"py/main.py");

# maincontent = mtmlparser();

# maincontent.readonefile("templates/test.cpp");

# print maincontent.disp() ;


#print pagehandler("index").call();

