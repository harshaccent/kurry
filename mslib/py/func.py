execfile(_mslib+"py/use.py");
execfile(_mslib+"py/sql.py");

fold = fold_l;

def mprint(*x):
	global _printout;
	_printout += (", ".join(str(i) for i in x));

def gkeys(a):
	return range(len(a)) if type(a) == list else a.keys();

def mmap(f, l, odict = False):
	return fold(lambda x,y: seta(x, l[y] if odict else y , f(l[y], y) ), gkeys(l), {} if (type(l) != list or odict) else [] );

def s(varn, val): #varn is a string, name of variable, val is value to be set to variable. | dl = [sets] | output: set the global variable
	exec("global " + varn);
	varn = val;

def doifcan(fun, inp, defaultval = None): #dl = [s2j] | run fun on inp if possible.
	try:
		return fun(*inp) if type(inp) == tuple else fun(inp);
	except:
		return defaultval;

def getitem(arr, key, defaultval = None): #arr can be list or dict | output = arr[key]
	return doifcan(lambda l,i: l[i], (arr, key), defaultval);

g = getitem; # dl = [get, ses, post] 

def has_key(arr, key): #is key set in arr ( List or dict)
	return doifcan(lambda l,i: (lambda x: True)(l[i]), (arr, key), False);

isg = has_key;

for i in ["get", "ses", "post"]:#defining 6 functions. get, ses, post, isget, isses, ispost
	exec("{0} = lambda key, defaultval = None: g({0}data, key, defaultval) ".format(i) );
	exec("is{0} = lambda key: {0}data.has_key(key) ".format(i) );

def sets(val, key = None, var = "sesdata"): #set given key of sesdata, if not given, set whole session.
	s( var, val) if key == None else seta( globals()[var], key, val )

def s2j(inp): #dl = []
	return doifcan(json.loads, inp);

def f(inp, var = "x"): #dl = [lelm], return function having inp as return value.
	return eval("lambda " + var + ":"+inp);

def arr2options(arr, typ = 'int'):
	return mmap(lambda x,i: {'dt': x, 'val': i+1 if typ == 'int' else x}, arr);

a2o = arr2options;

def gl(arr, keys, defaultval = None): #apply list of keys ex: gl(arr, ["x", 1, "y"]) = arr["x"][1]["y"]
	return fold(lambda x,y: g(x, y, defaultval), keys, arr);

def rift(var, val, checker):
	return val if checker(var) else var;

def rifn(var, val):
	return rift(var, val, lambda var: var == None );

tnow = timenow;

t2f = time2format;

s2t = str2time;

def timeondate(d, m, y):
	return s2t(str(d)+"-"+str(m)+"-"+str(y));

def gen_form(*args):
	return map(lambda x: ''.join(list(str(i) for i in x)), itertools.product(*args));

def sifu(arr, key, val, isforce = False):
	if (not isg(arr, key)) or isforce:
		if type(arr) == list and key > len(arr)-1:
			return fold(lambda x, y: r1(x.append(None if len(x)!=key else val), x), range(key-len(arr)+1), arr);
		else:
			arr[key] = val;
	return arr;

def seta(arr, key, val):#Set Array Keys. dl=[sets]
	return sifu(arr, key, val, True);

def r1(*args):
	return args[-1];

def rifu(arr, key, val, isforce = False):
	return sifu(copy.deepcopy(arr), key, val, isforce);

def mifu(a1, a2, isforce = False):# Merge If Unset
	return fold(lambda x1, yval, y1: sifu(x1, y1, yval, isforce), a2, a1);

def rmifu(a1, a2, isforce = False):
	return mifu(copy.deepcopy(a1), a2, isforce);

def msplit(st, spliter = '-'):
	return rift(st.split(spliter), [], f('x==[""]'));

def intsplit(st, llimit = None, ulimit = None):
	return filter(f('x!=None and ({0} == None or {0}<=x) and ({1} == None or x<={1})'.format(llimit, ulimit)), map(f('doifcan(int, x)'), msplit(st)));

t2f_date = lambda tat=None: time2format("%d-%m-%Y", tat);

def table(tname):
	return 'select * from '+tname;

def tf(x):
	return str(bool(x));

def rit(toprint, cond=True, toprint_false=''):
	return (toprint if cond else toprint_false)

def convchars(inp):
	return replaceall(inp, {"&": "&amp;", '"': "&quot;", "'": "&#039;", "<": "&lt;", ">": "&gt;"});

def mjoin(glu, l, defaultval=''):
	return glu.join(list(str(x) for x in l)) if len(l) > 0 else defaultval;

def index(l):
	return (l.keys() if type(l) == dict else range(len(l)));

def iem(con, exp):
	for i in index(con):
		if(con[i]):
			return exp[i];
	else:
		return exp[len(con)];

def gtable(name, astable = True):
	return "("+queries[name]+")"+name if astable else queries[name];


def isallone(l):
	return sum(l) == len(list(l));



#sql = sqllib();
#print sql.sval("users", limit=1);

#print sql.ival("users", {"name": "Mohit#$%^6''", "email": "timepass@mail.com"});


#sql.close_db();
