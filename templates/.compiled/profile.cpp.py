#This code is auto generated code, don't Edit it 
outpvar.cur.addfcdata("main2");
outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs({})));
outpvar.cur.fcalldata["main2"].cur.addfcdata("header4");
outpvar.cur.fcalldata["main2"].addchilds(newtag_header4({}, ginp, outpvar.cur.fcalldata["main2"].cur.fcalldata["header4"].root.content).root.content);
if (int((ginp["uid"] > 0))): 
  outpvar.cur.fcalldata["main2"].cur.addfcdata("profile_chef");
  outpvar.cur.fcalldata["main2"].addchilds(newtag_profile_chef({}, ginp, outpvar.cur.fcalldata["main2"].cur.fcalldata["profile_chef"].root.content).root.content);
outpvar.cur.fcalldata["main2"].close();
outpvar.addchilds(newtag_main2({"js": ["js/profile.js"], "htmlstyle": {"overflow-y": "scroll"}}, ginp, outpvar.cur.fcalldata["main2"].root.content).root.content);