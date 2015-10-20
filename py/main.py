
class pagehandler:
	def __init__(self, name):
		self.name = name;
		if(False and _server == "gcl"):
			elc("python client.py 10.208.20.186 ./compile");
		self.jsdata = {"HOST": HOST, "BASE": BASE, "curpage": self.name, "_server": _server};
		self.methodmap = {"index": self.index};

	def call(self):
		return sifu(( rifn(self.methodmap[self.name](), {}) if self.methodmap.has_key(self.name) else {}), "jsdata", json.dumps(self.jsdata));

	def index(self):
		allcatg = {"Kids":{"Dance":["Dance1", "Dance2"], "Photography":["Photo1", "Photo2"]}, "Adults":{"Dance":["Dance1", "Dance2"], "Photography":["Photo1", "Photo2"]}, "Pets":{"Dance":["Dance1", "Dance2"], "Photography":["Photo1", "Photo2"]} };
		icons = {"Kids": "photo/kid1.png", "Adults": "photo/adult1.png", "Pets": "photo/dog1.png"};
		catgs = list({"name":i, "icon":icons[i], "child": list({"name":j, "child": allcatg[i][j]} for j in allcatg[i])} for i in allcatg)
		return {"catg": catgs};

