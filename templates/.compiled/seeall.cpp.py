#This code is auto generated code, don't Edit it 
outpvar.cur.addfcdata("main1");
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "container"})));
for i in forlist(ginp["allt"]) :
  outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": ""})));
  outpvar.cur.fcalldata["main1"].cur.addfcdata("table1");
  outpvar.cur.fcalldata["main1"].addchilds(newtag_table1({"thead": i["data"]["thead"], "rows": i["data"]["rows"], "class": "bordered"}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["table1"].root.content).root.content);
  outpvar.cur.fcalldata["main1"].close();
  outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].close();
outpvar.addchilds(newtag_main1({}, ginp, outpvar.cur.fcalldata["main1"].root.content).root.content);