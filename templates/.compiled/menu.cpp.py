#This code is auto generated code, don't Edit it 
outpvar.cur.addfcdata("main2");
outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([]))));
outpvar.cur.fcalldata["main2"].cur.addfcdata("header4");
outpvar.cur.fcalldata["main2"].addchilds(newtag_header4(cod([]), ginp, outpvar.cur.fcalldata["main2"].cur.fcalldata["header4"].root.content).root.content);
outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([]))));
outpvar.cur.fcalldata["main2"].open(htmlnode("nav", extentattrs(cod([("class", "white"), ("attr", cod([("role", "container")])), ("style", cod([("border-bottom", "solid #ccc 1px")]))]))));
outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([("class", "nav-wrapper container")]))));
outpvar.cur.fcalldata["main2"].open(htmlnode("ul", extentattrs(cod([("class", "")]))));
outpvar.cur.fcalldata["main2"].open(htmlnode("li", extentattrs(cod([]))));
outpvar.cur.fcalldata["main2"].open(htmlnode("a", extentattrs(cod([("class", "dropdown-button"), ("attr", cod([("data-activates", "dropdown2"), ("aria-expanded", "false"), ("aria-haspopup", "true")]))]))));
outpvar.cur.fcalldata["main2"].addtext(myadd(myadd(("&nbsp;" * 20), ginp["day5times"]["textl"][0]), ("&nbsp;" * 0)));
outpvar.cur.fcalldata["main2"].cur.addfcdata("icon");
outpvar.cur.fcalldata["main2"].addchilds(newtag_icon(cod([("name", "arrow_drop_down"), ("aclass", "right")]), ginp, outpvar.cur.fcalldata["main2"].cur.fcalldata["icon"].root.content).root.content);
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].open(htmlnode("li", extentattrs(cod([]))));
outpvar.cur.fcalldata["main2"].open(htmlnode("a", extentattrs(cod([("class", "dropdown-button"), ("attr", cod([("data-activates", "dropdown3")]))]))));
outpvar.cur.fcalldata["main2"].addtext(myadd(myadd(("&nbsp;" * 18), "All"), ("&nbsp;" * 0)));
outpvar.cur.fcalldata["main2"].cur.addfcdata("icon");
outpvar.cur.fcalldata["main2"].addchilds(newtag_icon(cod([("name", "arrow_drop_down"), ("aclass", "right")]), ginp, outpvar.cur.fcalldata["main2"].cur.fcalldata["icon"].root.content).root.content);
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].open(htmlnode("ul", extentattrs(cod([("attr", cod([("id", "dropdown3")])), ("class", "dropdown-content")]))));
foodtype = ["All", "Veg", "Non-Veg"];
for ii in forlist(foodtype, True ) :
  i = foodtype[ii];
  outpvar.cur.fcalldata["main2"].open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.fcalldata["main2"].open(htmlnode("a", extentattrs(cod([("attr", cod([("href", "")]))]))));
  outpvar.cur.fcalldata["main2"].addtext(i);
  outpvar.cur.fcalldata["main2"].close();
  outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].open(htmlnode("ul", extentattrs(cod([("attr", cod([("id", "dropdown2")])), ("class", "dropdown-content")]))));
for ii in forlist(ginp["day5times"]["timel"], True ) :
  i = ginp["day5times"]["timel"][ii];
  outpvar.cur.fcalldata["main2"].open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.fcalldata["main2"].open(htmlnode("a", extentattrs(cod([("attr", cod([("href", myadd(myadd(ginp["BASE"], "menu?datetime="), i))]))]))));
  outpvar.cur.fcalldata["main2"].addtext(ginp["day5times"]["textl"][ii]);
  outpvar.cur.fcalldata["main2"].close();
  outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([("class", "container-fluid")]))));
outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([("class", "row")]))));
outpvar.cur.fcalldata["main2"].open(htmlnode("ul", extentattrs(cod([("class", "tabs")]))));
outpvar.cur.fcalldata["main2"].cur.addfcdata("disptabs");
outpvar.cur.fcalldata["main2"].addchilds(newtag_disptabs(cod([("liclass", "tab col s2"), ("tabname", ["Lunch", "Dinner"]), ("tablink", ["#lunch", "#dinner"])]), ginp, outpvar.cur.fcalldata["main2"].cur.fcalldata["disptabs"].root.content).root.content);
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([("class", "container-fluid")]))));
outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([("class", "row")]))));
outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([("class", "col l10 offset-l1 s10 m10 offset-s1 offset-m1")]))));
outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([("attr", cod([("id", "lunch")]))]))));
outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([("class", "row"), ("attr", cod([("align", "center")]))]))));
if (int((len(ginp["lunch"]) == 0))): 
  outpvar.cur.fcalldata["main2"].cur.addfcdata("menu_nofood");
  outpvar.cur.fcalldata["main2"].addchilds(newtag_menu_nofood(cod([]), ginp, outpvar.cur.fcalldata["main2"].cur.fcalldata["menu_nofood"].root.content).root.content);
for i in forlist(ginp["lunch"], False ) :
  outpvar.cur.fcalldata["main2"].cur.addfcdata("dispfood");
  outpvar.cur.fcalldata["main2"].addchilds(newtag_dispfood(cod([("dishinfo", i)]), ginp, outpvar.cur.fcalldata["main2"].cur.fcalldata["dispfood"].root.content).root.content);
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([("attr", cod([("id", "dinner")]))]))));
outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([("class", "row"), ("attr", cod([("align", "center")]))]))));
if (int((len(ginp["dinner"]) == 0))): 
  outpvar.cur.fcalldata["main2"].cur.addfcdata("menu_nofood");
  outpvar.cur.fcalldata["main2"].addchilds(newtag_menu_nofood(cod([]), ginp, outpvar.cur.fcalldata["main2"].cur.fcalldata["menu_nofood"].root.content).root.content);
for i in forlist(ginp["dinner"], False ) :
  outpvar.cur.fcalldata["main2"].cur.addfcdata("dispfood");
  outpvar.cur.fcalldata["main2"].addchilds(newtag_dispfood(cod([("dishinfo", i)]), ginp, outpvar.cur.fcalldata["main2"].cur.fcalldata["dispfood"].root.content).root.content);
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].close();
outpvar.addchilds(newtag_main2(cod([("js", ["js/menu.js"]), ("htmlstyle", cod([("overflow-y", "scroll")]))]), ginp, outpvar.cur.fcalldata["main2"].root.content).root.content);