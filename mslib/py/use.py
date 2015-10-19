def fold_l(f, l, a):
	for i in l:
		a = f(a, i) if len(inspect.getargspec(f).args) == 2 else f(a, l[i], i);
	return a;

def timenow():
	return int(mktime(datetime.datetime.now(_localtz).timetuple()));

def time2format(formate, tat = None):#tat: TimeAt
	return datetime.datetime.fromtimestamp(rifn(tat, tnow())).strftime(formate);

def str2time(times, formate = None):
	formates = gen_form(['']+gen_form(['%d-%m-'], ['%y', '%Y']), [' '], ['', '%I:%M:%S %p', '%H:%M:%S', '%I:%M %p', '%H:%M' ])
	return (lambda x: x if type(x) == int else 0 )(fold( lambda x,y: rifn(doifcan(lambda x,y: int(time.mktime(datetime.datetime.strptime(x,y.strip()).timetuple())) , (x, y)), x), formates, re.sub('\s+', ' ', times).strip()));

def daystarttime(tat = None):
	return s2t(t2f_date(tat));

def grouplist(arr, gap=1):
	outp = [];
	for i in arr:
		if (outp == [] or (outp[-1][0] + outp[-1][1]*gap != i)):
			outp.append([i, 1]);
		else:
			outp[-1][1]+=1;
	return outp;

def sql2dict(data, key):
	return fold(lambda x,y: sifu(x, y[key], y, True), data, {});

def replaceall(inp, ra):
	return fold(lambda s, ar, br: s.replace(br, ar), ra, inp);

def searchkeysplit(ss):
	return re.split("[^a-zA-Z0-9]+", ss.strip().lower());

def seto(a, b, o='|'):#Set operation, Warning: list order not preserved.
	return eval('list(set(a) '+o+' set(b) )');


def pkey(arr, keys):# partial keys
	return (mmap(lambda x, y: arr[x], seto(keys, gkeys(arr), '&'), True));

def readfd(fd):
	data=fd.read();
	fd.close();
	return data;

def writefd(fd,data):
	fd.write(data);
	fd.close();

def read_file(fn):
	return readfd(open(fn));

def write_file(fn,data):
	writefd(open(fn,'w'),data);

def elc(c):
	return readfd(os.popen(c));

class mnum(int):#Same as int, except it thinks, -1 is infinite
	def __init__(self, ival):
		self.val = ival;
	def __str__(self):
		return str(self.val);
	def __add__(self, x):
		return mnum(-1) if self.val == -1 or mnum(x).val == -1 else mnum(self.val+x)

	def __sub__(self, x):
		return self+mnum(-x);

	def __cmp__(self, x):
		x=mnum(x);
		if(self.val == -1):
			return 1;
		elif(x.val == -1):
			return -1;
		elif(self.val == x.val):
			return 0;
		elif(self.val < x.val):
			return -1;
		else:
			return 1;

def allfile_rec(f):
	if(f[-1] != "/"):
		f+="/";
	allff = os.listdir(f);
	return list(f+i for i in allff if os.path.isfile(f+i))+fold(lambda x,y: x+y, list(allfile_rec(f+i) for i in allff if not(os.path.isfile(f+i)) ), [])
