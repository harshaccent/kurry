
class server_action:
	def handler(self, cmd):
		self.ec = 1;
		computed = eval("self."+cmd["action"]+"(cmd)");
		return {"ec": self.ec, "data": computed};

	def tnow(self, cmd):
		return tnow();

	def sql(self, cmd):
		return "This is query output";
		return _sql.sval("users", limit=1);

