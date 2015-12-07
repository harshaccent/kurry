#This code is auto generated code, don't Edit it 
outpvar.cur.addfcdata("main2");
outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs({})));
outpvar.cur.fcalldata["main2"].cur.addfcdata("header4");
outpvar.cur.fcalldata["main2"].addchilds(newtag_header4({}, ginp, outpvar.cur.fcalldata["main2"].cur.fcalldata["header4"].root.content).root.content);
if (int((ginp["islogin"] == "a"))): 
  outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs({"class": "continer"})));
  outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs({"class": "col l8 offset-l2 m10 offset-m1 s12"})));
  outpvar.cur.fcalldata["main2"].cur.addfcdata("account_admin");
  outpvar.cur.fcalldata["main2"].addchilds(newtag_account_admin({"users": ginp["users"]}, ginp, outpvar.cur.fcalldata["main2"].cur.fcalldata["account_admin"].root.content).root.content);
  outpvar.cur.fcalldata["main2"].close();
  outpvar.cur.fcalldata["main2"].close();
  outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].close();
outpvar.addchilds(newtag_main2({"js": ["js/menu.js"], "htmlstyle": {"overflow-y": "scroll"}}, ginp, outpvar.cur.fcalldata["main2"].root.content).root.content);