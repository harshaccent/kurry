_agent = "gcl";

execfile("includes/setting.py");
execfile(_mslib+"py/func.py");
execfile("mslib/ocaml/run.py");
execfile(ROOT+"py/main.py");

# maincontent = mtmlparser();

# maincontent.readonefile("templates/test.cpp");

# print maincontent.disp() ;


#print sql.sval("users", limit=1);

#print sql.ival("users", {"name": "Mohit#$%^6''", "email": "timepass@mail.com"});

#a = pagehandler("init").init();

[query, darr, arr] = eval(read_file(".queryinput.txt"));
if(sys.argv[1] == 'g'):
	outp = _sql.g(query, darr, arr);
else:
	outp = _sql.q(query, darr, arr);
write_file(".queryoutput.txt", str(outp));


_sql.close_db();
