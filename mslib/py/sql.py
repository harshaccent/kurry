class sqllib:
	db = None;
	cur = None;
	#i_ : internal local methods.
	def init_db(self):
		if(self.db == None and self.cur == None):
			self.db = MySQLdb.connect(host="poorvi.cse.iitd.ac.in", user="mohit", passwd="mohitsaini", db="mohit");
			self.cur = self.db.cursor(MySQLdb.cursors.DictCursor);

	def close_db(self):
		map(f('x.close() if x!=None else None'), [self.cur, self.db]);

	def rquery(self, query, dkeys={}, keys={}):
		return fold(lambda q,tr: q.replace("{"+tr+"}", "%("+tr+")s" if isg(dkeys, tr) else g(keys, tr, '{'+tr+"}")), (x[1:-1] for x in re.compile("{[^}]+}").findall(query)), query);

	def q(self, query, darr={}, arr={}):
		self.init_db();
		self.cur.execute(self.rquery(query, darr, arr), darr)
		self.db.commit();
		return (self.cur.lastrowid + self.cur.rowcount)

	def g(self, query, darr={}, arr={}):
		self.init_db();
		self.cur.execute(self.rquery(query, darr, arr), darr);
		return list(self.cur)

	def g1(self, query, darr={}, arr={}):
		return self.i_1row(self.g(query, darr, arr), 1);

	def i_conds(self, arr, glu = ' AND '):
		if(type(arr) == dict):
			(a,b) = fold(lambda (clist, darr),val,key: r1(clist.append(key+" = {"+key+"}"), (clist, seta(darr, key, val))) , arr, ([],{}));
			return (mjoin(glu, a, "true"), b);
		else:
			return (arr, {});

	def i_1row(self, x, limit):
		return (g(x, 0) if limit == 1 else x);

	def i_limits(self, limit):
		return '' if limit == -1 else 'limit '+str(limit);

	def sval(self, table, flds = '*', conds={}, limit = -1):
		(s_conds, darr) = self.i_conds(conds);
		query = "select {1} from {0} where {2} {3}".format(table, flds, s_conds, self.i_limits(limit) );
		return self.i_1row(self.g(query, darr), limit);

	def uval(self, table, toset, conds={}, limit = -1):
		[(s_conds, darr), (s_set, darr1)] = map(f('self.i_conds(*x)'), [(conds, ' AND '), (toset, ',')]);
		return self.i_1row(self.q("update {table} set {s_set} where {s_conds} {limit_s}".format( **rmifu(locals(),{"limit_s": self.i_limits(limit)})), mifu(darr, darr1)), limit);

	def dval(self, table, conds={}, limit = -1):
		(s_conds, darr) = self.i_conds(conds);
		return self.i_1row(self.q("delete from {table} where {s_conds} {limit_s}".format( **rmifu(locals(), {"limit_s": self.i_limits(limit)}) ), darr), limit);

	def ival(self, table, toins={}):
		return self.q("insert into {0} ({1}) values ({2})".format( *([table]+map(lambda l:','.join(l), (lambda l:[l, list("{"+x+"}" for x in l)])(toins.keys())) )), toins);

	def autoscroll(self, query, darr={}, key = None, sort='', isloadold = True, minl = None, maxl = None, arr={}):
		(minl, maxl) = tuple(mmap(lambda x, y: rifu(x, [minl, maxl][y])  ,list(pkeys(arr, ["minl", "maxl"]))))

	# 	setifnn($minl, $param["minl"]);
	# 	setifnn($maxl, $param["maxl"]);
	# 	if($key!=null){
	# 		if($isloadold)
	# 			$querylimit = "select * from (".gtable($query, false).") outpquery where ($key<{min} OR {min}=-1) ".($param["minl"]==-1?'':"limit {minl} ");
	# 		else
	# 			$querylimit = "select * from (".gtable($query, false).") outpquery where $key>{max} ".($param["maxl"]==-1?'':"limit {maxl} ");
	# 	} else{//max,maxl must be +ve int
	# 		$querylimit="select * from (".$query.") outpquery limit {maxl} offset {max} ";
	# 	}
	# 	if($key!=null)
	# 		$querysort="select * from (".$querylimit.") sortquery ".$sort;
	# 	else
	# 		$querysort=$querylimit;
	# 	$qresult=self.::getA($querysort,$param);
	# 	$outp["qresult"]=$qresult;
	# 	$outp["maxl"]=$maxl;
	# 	$outp["minl"]=$minl;
	# 	$outp["qresultlen"]=count($qresult);
	# 	if($key==null){
	# 		$outp["max"]=$param["max"]+$param["maxl"];
	# 	} else{
	# 		if(count($qresult)==0){
	# 			$outp["min"] = $param["min"];
	# 			$outp["max"] = $param["max"];
	# 		} else{
	# 			$e1=$qresult[0][$key];
	# 			$e2=$qresult[count($qresult)-1][$key];
	# 			$s=new Special();
	# 			$outp["min"] = $s->min($e1, $e2, $param["min"]);
	# 			$outp["max"] = $s->max($e1, $e2, $param["max"]);
	# 		}
	# 	}
	# 	return $outp;
	# }
