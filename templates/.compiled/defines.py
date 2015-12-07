#This code is auto generated code, don't Edit it 
def newtag_main(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("acss", ["css/materialize.min.css", "css/lib.css", "css/materialize.min.css", "css/custom-stylesheet.css", "css/jquery.bxslider.css", "https://fonts.googleapis.com/icon?family=Material+Icons", "css/lib.css", "css/main.css", "css/style.css"]), ("ajs", ["mslib/js/jquery-2.1.1.min.js", "mslib/js/materialize.min.js", "mslib/js/jquery.bxslider.min.js", "mslib/js/jquery.easing.1.3.js", "mslib/js/jquery.raty.js", "mslib/js/lib.js", "mslib/js/mohit.js", "mslib/js/mohitlib.js", "mslib/js/main.js"]), ("title", "Class Pundit"), ("css", []), ("js", []), ("bodystyle", cod([])), ("htmlstyle", cod([]))])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  inp["css"] = myadd(inp["acss"], inp["css"]);
  inp["js"] = myadd(inp["ajs"], inp["js"]);
  outpvar.addtext("<!DOCTYPE html>");
  outpvar.open(htmlnode("html", extentattrs(cod([("style", inp["htmlstyle"])]))));
  outpvar.open(htmlnode("head", extentattrs(cod([]))));
  outpvar.open(htmlnode("base", extentattrs(cod([("attr", cod([("href", inp["HOST"])]))]))));
  outpvar.open(htmlnode("title", extentattrs(cod([]))));
  outpvar.addtext(inp["title"]);
  outpvar.close();
  for i in forlist(inp["css"], False ) :
    outpvar.open(htmlnode("link", extentattrs(cod([("attr", cod([("href", i), ("rel", "stylesheet"), ("type", "text/css")]))]))));
  outpvar.close();
  outpvar.open(htmlnode("body", extentattrs(cod([("style", inp["bodystyle"])]))));
  outpvar.addchilds(innerHTML);
  outpvar.open(htmlnode("script", extentattrs(cod([("attr", cod([("type", "text/javascript")]))]))));
  outpvar.addtext(myadd(myadd("var jsdata = ", inp["jsdata"]), ";"));
  outpvar.close();
  outpvar.open(htmlnode("script", extentattrs(cod([("attr", cod([("type", "text/javascript")]))]))));
  outpvar.addtext("var ec  = jsdata['_ec'] ;");
  outpvar.close();
  for i in forlist(inp["js"], False ) :
    outpvar.open(htmlnode("script", extentattrs(cod([("attr", cod([("type", "text/javascript"), ("src", i)]))]))));
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_disptabs(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tabname", []), ("tablink", []), ("liclass", None), ("active", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  for j in forlist(inp["tabname"], True ) :
    i = inp["tabname"][j];
    outpvar.open(htmlnode("li", extentattrs(cod([("class", inp["liclass"])]))));
    inp["isactive"] = ("active" if (int((inp["active"] == inp["tablink"][j]))) else " ");
    outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("href", inp["tablink"][j])])), ("class", inp["isactive"])]))));
    outpvar.addtext(i);
    outpvar.close();
    outpvar.close();
  return outpvar;
  
def newtag_header1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tabname", []), ("tablink", [])])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "navbar-fixed ")]))));
  outpvar.open(htmlnode("nav", extentattrs(cod([("class", "white"), ("attr", cod([("role", "container")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "nav-wrapper container")]))));
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("id", "logo-container"), ("href", inp["HOST"])])), ("class", "brand-logo")]))));
  outpvar.open(htmlnode("img", extentattrs(cod([("attr", cod([("src", "photo/mylogo1.png")])), ("class", "circle responsive-img"), ("style", cod([("vertical-align", "middle")]))]))));
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("class", "right hide-on-med-and-down")]))));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("tabname", inp["tabname"]), ("tablink", inp["tablink"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_header1_cp(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tabname", []), ("tablink", [])])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "navbar-fixed ")]))));
  outpvar.open(htmlnode("nav", extentattrs(cod([("class", "white"), ("attr", cod([("role", "container")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "nav-wrapper container")]))));
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("id", "logo-container"), ("href", inp["HOST"])])), ("class", "brand-logo")]))));
  outpvar.open(htmlnode("img", extentattrs(cod([("attr", cod([("src", "photo/mylogo1.png")])), ("class", "circle responsive-img"), ("style", cod([("vertical-align", "middle")]))]))));
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("class", "right hide-on-med-and-down")]))));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("tabname", inp["tabname"]), ("tablink", inp["tablink"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.cur.addfcdata("headertabs_cp");
  outpvar.addchilds(newtag_headertabs_cp(cod([]), ginp, outpvar.cur.fcalldata["headertabs_cp"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("id", "nav-mobile"), ("class", "side-nav")]))));
  outpvar.cur.addfcdata("headertabs_cp");
  outpvar.addchilds(newtag_headertabs_cp(cod([]), ginp, outpvar.cur.fcalldata["headertabs_cp"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("data-activates", "nav-mobile")])), ("class", "button-collapse")]))));
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon(cod([("name", "menu")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_icon(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("aclass", "")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("i", extentattrs(cod([("class", myadd("material-icons ", inp["aclass"])), ("style", inp["style"])]))));
  outpvar.addtext(inp["name"]);
  outpvar.close();
  return outpvar;
  
def newtag_icon1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("class", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  inp["attr"]["src"] = inp["img"];
  outpvar.open(htmlnode("img", extentattrs(cod([("attr", inp["attr"]), ("style", cod([("margin-bottom", "-5px")])), ("class", inp["class"])]))));
  return outpvar;
  
def newtag_checkbox1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("checked", None), ("label", "Check"), ("aclass", ""), ("labels", cod([]))])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("span", extentattrs(cod([]))));
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("type", "checkbox"), ("id", inp["id"]), ("checked", inp["checked"])])), ("class", myadd("filled-in ", inp["aclass"])), ("data", inp["data"])]))));
  outpvar.open(htmlnode("label", extentattrs(cod([("attr", cod([("for", inp["id"])])), ("style", inp["labels"])]))));
  outpvar.addtext(inp["label"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_checkbox2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("checked", None), ("label", "Check"), ("aclass", ""), ("labels", cod([]))])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("span", extentattrs(cod([]))));
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("type", "radio"), ("id", inp["id"]), ("checked", inp["checked"])])), ("class", myadd("with-gap ", inp["aclass"])), ("data", inp["data"])]))));
  outpvar.open(htmlnode("label", extentattrs(cod([("attr", cod([("for", inp["id"])])), ("style", inp["labels"])]))));
  outpvar.addtext(inp["label"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_bigf(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("font", "65px")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("span", extentattrs(cod([("style", cod([("font-size", inp["font"]), ("text-shadow", "3px 3px 3px #000, 2px 2px 2px blue")])), ("color", inp["color"])]))));
  outpvar.addtext(inp["name"]);
  outpvar.close();
  return outpvar;
  
def newtag_bigf1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("font", "40px")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.cur.addfcdata("bigf");
  outpvar.addchilds(newtag_bigf(cod([("color", inp["color"]), ("font", inp["font"]), ("name", inp["name"])]), ginp, outpvar.cur.fcalldata["bigf"].root.content).root.content);
  return outpvar;
  
def newtag_height(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("height", myadd(inp["val"], "px"))]))]))));
  outpvar.close();
  return outpvar;
  
def newtag_resimg(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("aclass", ""), ("opacity", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("img", extentattrs(cod([("class", myadd("responsive-img ", inp["aclass"])), ("attr", cod([("src", inp["src"])])), ("style", cod([("opacity", inp["opacity"])]))]))));
  return outpvar;
  
def newtag_circleimg(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("opacity", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.cur.addfcdata("resimg");
  outpvar.addchilds(newtag_resimg(cod([("aclass", "circle"), ("src", inp["src"]), ("opacity", inp["opacity"])]), ginp, outpvar.cur.fcalldata["resimg"].root.content).root.content);
  return outpvar;
  
def newtag_divpedding(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("text", ""), ("padding", "5px")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("padding", inp["padding"])])), ("class", inp["class"])]))));
  outpvar.addtext(inp["text"]);
  outpvar.addchilds(innerHTML);
  outpvar.close();
  return outpvar;
  
def newtag_textdiv(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("text", ""), ("fontw", None), ("font", None), ("color", None), ("class", None), ("id", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("font-size", inp["font"]), ("font-weight", inp["fontw"])])), ("color", inp["color"]), ("class", inp["class"]), ("id", inp["id"])]))));
  outpvar.addchilds(innerHTML);
  outpvar.addtext(inp["text"]);
  outpvar.close();
  return outpvar;
  
def newtag_textdiv1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("font", "20px"), ("fontw", None), ("color", None), ("class", None), ("text", "")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv(cod([("font", inp["font"]), ("fontw", inp["fontw"]), ("color", inp["color"]), ("class", inp["class"]), ("text", inp["text"])]), ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  return outpvar;
  
def newtag_a1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("class", None), ("text", None), ("href", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", inp["attr"]), ("style", inp["style"]), ("class", inp["class"])]))));
  outpvar.addtext(inp["text"]);
  outpvar.close();
  return outpvar;
  
def newtag_starrating(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("val", 5)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  for i in forlist(inp["val"], False ) :
    outpvar.open(htmlnode("img", extentattrs(cod([("attr", cod([("src", "photo/rating4.png")])), ("style", cod([("margin", "-1px"), ("width", "22px")]))]))));
  return outpvar;
  
def newtag_input1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("aclass", "col s6"), ("type", "text"), ("dc", "simple"), ("icon", None), ("dname", None), ("value", None), ("iclass", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", myadd("input-field ", inp["aclass"]))]))));
  if (inp["icon"]): 
    outpvar.cur.addfcdata("icon");
    outpvar.addchilds(newtag_icon(cod([("name", inp["icon"]), ("aclass", "prefix")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  inp["data"]["name"] = inp["label"];
  inp["data"]["dc"] = inp["dc"];
  if (int((inp["dname"] != None))): 
    inp["data"]["name"] = inp["dname"];
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("id", inp["id"]), ("type", inp["type"]), ("value", inp["value"])])), ("class", inp["iclass"]), ("data", inp["data"])]))));
  outpvar.open(htmlnode("label", extentattrs(cod([("attr", cod([("for", inp["id"])]))]))));
  outpvar.addtext(inp["label"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_input2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("aclass", "col s6"), ("type", "text")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", myadd("input-field ", inp["aclass"]))]))));
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("id", inp["id"]), ("type", inp["type"]), ("name", inp["id"])])), ("class", inp["iclass"])]))));
  outpvar.open(htmlnode("label", extentattrs(cod([("attr", cod([("for", inp["id"])]))]))));
  outpvar.addtext(inp["label"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_input3(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("aclass", "col s6"), ("type", "text"), ("dc", "simple"), ("icon", None), ("dname", None), ("value", None), ("iclass", ""), ("name", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", myadd("input-field ", inp["aclass"]))]))));
  if (inp["icon"]): 
    outpvar.cur.addfcdata("icon");
    outpvar.addchilds(newtag_icon(cod([("name", inp["icon"]), ("aclass", "prefix")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  inp["data"]["name"] = inp["label"];
  inp["data"]["dc"] = inp["dc"];
  if (int((inp["dname"] != None))): 
    inp["data"]["name"] = inp["dname"];
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("type", inp["type"]), ("value", inp["value"]), ("placeholder", inp["label"]), ("name", inp["name"])])), ("class", myadd("inputph ", inp["iclass"])), ("data", inp["data"])]))));
  outpvar.close();
  return outpvar;
  
def newtag_textarea1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("aclass", "col l12 m12 s12")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", myadd("input-field ", inp["aclass"]))]))));
  outpvar.open(htmlnode("textarea", extentattrs(cod([("attr", cod([("id", inp["id"]), ("name", inp["id"])])), ("class", "materialize-textarea")]))));
  outpvar.close();
  outpvar.open(htmlnode("label", extentattrs(cod([("attr", cod([("for", inp["id"])]))]))));
  outpvar.addtext(inp["label"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_button1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("aclass", "")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("button", extentattrs(cod([("class", myadd("btn waves-effect waves-light btn ", inp["aclass"])), ("data", inp["data"]), ("attr", inp["attr"]), ("datas", inp["datas"])]))));
  outpvar.addtext(inp["name"]);
  outpvar.close();
  return outpvar;
  
def newtag_main1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("css", []), ("js", []), ("bodystyle", cod([])), ("htmlstyle", cod([])), ("title", "KurryBox")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  inp["js"] = myadd(["js/main.js"], inp["js"]);
  outpvar.cur.addfcdata("main");
  outpvar.cur.fcalldata["main"].addchilds(innerHTML);
  outpvar.addchilds(newtag_main(cod([("title", inp["title"]), ("css", inp["css"]), ("js", inp["js"]), ("bodystyle", inp["bodystyle"]), ("htmlstyle", inp["htmlstyle"])]), ginp, outpvar.cur.fcalldata["main"].root.content).root.content);
  return outpvar;
  
def newtag_main2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("css", []), ("js", []), ("bodystyle", cod([])), ("htmlstyle", cod([])), ("title", "KurryBox")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  inp["js"] = myadd(["js/main.js"], inp["js"]);
  outpvar.cur.addfcdata("main");
  outpvar.cur.fcalldata["main"].addchilds(innerHTML);
  outpvar.cur.fcalldata["main"].cur.addfcdata("loginmodal");
  outpvar.cur.fcalldata["main"].addchilds(newtag_loginmodal(cod([]), ginp, outpvar.cur.fcalldata["main"].cur.fcalldata["loginmodal"].root.content).root.content);
  outpvar.addchilds(newtag_main(cod([("title", inp["title"]), ("css", inp["css"]), ("js", inp["js"]), ("bodystyle", inp["bodystyle"]), ("htmlstyle", inp["htmlstyle"]), ("acss", ["css/materialize.min.css", "css/lib.css", "css/materialize.min.css", "css/custom-stylesheet.css", "css/jquery.bxslider.css", "mslib/css/gfont.css", "css/lib.css", "css/main.css", "css/style.css"])]), ginp, outpvar.cur.fcalldata["main"].root.content).root.content);
  return outpvar;
  
def newtag_bigsearch(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row"), ("style", cod([("background-color", "")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l1 m1")]))));
  outpvar.open(htmlnode("p", extentattrs("&nbsp;")));
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col m8 s12 l9"), ("style", cod([("padding", "0px"), ("margin", "0px")]))]))));
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("placeholder", inp["ph"]), ("id", inp["id"]), ("autofocus", inp["autofocus"])])), ("class", "bigsearch definput"), ("style", cod([("border-radius", "0px")]))]))));
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col m2 s12 l1 "), ("style", cod([("padding", "0px"), ("margin", "0px")]))]))));
  outpvar.open(htmlnode("button", extentattrs(cod([("class", "bigsearchbutton waves-effect waves-light btn"), ("style", cod([("border-radius", "0px")])), ("attr", cod([("type", "submit")]))]))));
  outpvar.open(htmlnode("p", extentattrs("Go")));
  outpvar.close();
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon(cod([("name", "send"), ("aclass", "right")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_header4(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  if (int((inp["islogin"] == None))): 
    outpvar.cur.addfcdata("header2");
    outpvar.addchilds(newtag_header2(cod([("tablink", [myadd(inp["BASE"], "chefjoin")]), ("tabname", ["Be a Chef"]), ("tablink1", [""]), ("tabname1", ["Blog"])]), ginp, outpvar.cur.fcalldata["header2"].root.content).root.content);
  elif (int((inp["islogin"] == "u"))): 
    outpvar.cur.addfcdata("header2_user");
    outpvar.addchilds(newtag_header2_user(cod([("tablink", [inp["HOST"], "", "", myadd(inp["BASE"], "cart")]), ("tabname", ["Home", "Our Story", "Blog", "Cart"])]), ginp, outpvar.cur.fcalldata["header2_user"].root.content).root.content);
  elif (int((inp["islogin"] == "a"))): 
    outpvar.cur.addfcdata("header2_admin");
    outpvar.addchilds(newtag_header2_admin(cod([("tablink", [inp["HOST"], "", "", "", "", ""]), ("tabname", ["Home", "Our Story", "Blog"])]), ginp, outpvar.cur.fcalldata["header2_admin"].root.content).root.content);
  elif (int((inp["islogin"] == "c"))): 
    outpvar.cur.addfcdata("header2_chef");
    outpvar.addchilds(newtag_header2_chef(cod([("tablink", [inp["HOST"], "", "", "", "", ""]), ("tabname", ["Home", "Our Story", "Blog"])]), ginp, outpvar.cur.fcalldata["header2_chef"].root.content).root.content);
  return outpvar;
  
def newtag_header3(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tabname", []), ("tablink", [])])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "navbar-fixed ")]))));
  outpvar.open(htmlnode("nav", extentattrs(cod([("class", "white"), ("attr", cod([("role", "container")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "nav-wrapper container")]))));
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("id", "logo-container"), ("href", inp["BASE"])])), ("class", "brand-logo")]))));
  outpvar.open(htmlnode("img", extentattrs(cod([("attr", cod([("src", "photo/mylogo1.png")])), ("class", "circle responsive-img"), ("style", cod([("vertical-align", "middle")]))]))));
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("class", "right hide-on-med-and-down")]))));
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.open(htmlnode("a", extentattrs(cod([("class", "dropdown-button"), ("attr", cod([("data-activates", "dropdown2")]))]))));
  outpvar.open(htmlnode("p", extentattrs(myadd(myadd(("&nbsp;" * 10), "Today, 28th Oct"), ("&nbsp;" * 10)))));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.open(htmlnode("a", extentattrs(cod([("class", "dropdown-button"), ("attr", cod([("data-activates", "dropdown1")]))]))));
  outpvar.open(htmlnode("p", extentattrs(myadd(myadd(("&nbsp;" * 5), "All"), ("&nbsp;" * 20)))));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("tabname", inp["tabname"]), ("tablink", inp["tablink"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("attr", cod([("id", "dropdown1")])), ("class", "dropdown-content")]))));
  inp["foodtype"] = ["All", "Veg", "Non-Veg"];
  for ii in forlist(inp["foodtype"], True ) :
    i = inp["foodtype"][ii];
    outpvar.open(htmlnode("li", extentattrs(cod([]))));
    outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("href", "")]))]))));
    outpvar.open(htmlnode("p", extentattrs(i)));
    outpvar.close();
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("attr", cod([("id", "dropdown2")])), ("class", "dropdown-content")]))));
  inp["nextdays"] = ["Today, 26 Oct", "27 Oct", "28 Oct"];
  for ii in forlist(inp["nextdays"], True ) :
    i = inp["nextdays"][ii];
    outpvar.open(htmlnode("li", extentattrs(cod([]))));
    outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("href", "")]))]))));
    outpvar.open(htmlnode("p", extentattrs(i)));
    outpvar.close();
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_dispfood(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s12 l4 m6 "), ("style", cod([]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", " card-panel"), ("style", cod([("margin-bottom", "40px"), ("padding", "0px")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([]))));
  outpvar.cur.addfcdata("resimg");
  outpvar.addchilds(newtag_resimg(cod([("src", inp["dishinfo"]["pic"])]), ginp, outpvar.cur.fcalldata["resimg"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("padding-bottom", "10px")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("padding", "10px")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l8"), ("attr", cod([("align", "left")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([]))));
  outpvar.open(htmlnode("p", extentattrs(inp["dishinfo"]["title"])));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l4")]))));
  outpvar.cur.addfcdata("icon1");
  outpvar.addchilds(newtag_icon1(cod([("img", "photo/inr1.png")]), ginp, outpvar.cur.fcalldata["icon1"].root.content).root.content);
  outpvar.open(htmlnode("span", extentattrs(cod([("style", cod([("font-size", "25px"), ("font-weight", "600")]))]))));
  outpvar.open(htmlnode("p", extentattrs(inp["dishinfo"]["price"])));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row valign-wrapper"), ("attr", cod([("align", "left")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l2")]))));
  outpvar.cur.addfcdata("circleimg");
  outpvar.addchilds(newtag_circleimg(cod([("src", inp["dishinfo"]["profilepic"])]), ginp, outpvar.cur.fcalldata["circleimg"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l10")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("font-weight", "500")]))]))));
  outpvar.cur.addfcdata("profilea1");
  outpvar.addchilds(newtag_profilea1(cod([("name", myadd("Chef ", inp["dishinfo"]["name"])), ("uid", inp["dishinfo"]["cid"])]), ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([]))));
  outpvar.cur.addfcdata("starrating");
  outpvar.addchilds(newtag_starrating(cod([("val", 3)]), ginp, outpvar.cur.fcalldata["starrating"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  if (int((inp["islogin"] == "a"))): 
    outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l4 ")]))));
    outpvar.open(htmlnode("button", extentattrs(cod([("class", "btn waves-effect waves-light btn"), ("datas", cod([("datetime", inp["dishinfo"]["datetime"]), ("lord", inp["dishinfo"]["lord"]), ("dishid", inp["dishinfo"]["id"])])), ("data", cod([("onclick", "sreq"), ("action", "deletedisp"), ("restext", "Deleted !")]))]))));
    outpvar.open(htmlnode("p", extentattrs("Delete")));
    outpvar.close();
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l4 offset-l3")]))));
    outpvar.open(htmlnode("button", extentattrs(cod([("class", "btn waves-effect waves-light btn")]))));
    outpvar.open(htmlnode("p", extentattrs("Edit")));
    outpvar.close();
    outpvar.close();
    outpvar.close();
  elif (int((inp["loginid"] == inp["dishinfo"]["cid"]))): 
    pass
  elif (1): 
    outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l4 ")]))));
    outpvar.open(htmlnode("button", extentattrs(cod([("class", "btn waves-effect waves-light btn"), ("data", cod([("onclick", "addfav")])), ("attr", cod([("id", "mohit")]))]))));
    outpvar.open(htmlnode("p", extentattrs("Favourite")));
    outpvar.close();
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l4 offset-l3")]))));
    outpvar.open(htmlnode("button", extentattrs(cod([("class", "btn waves-effect waves-light btn"), ("data", cod([("onclick", "sreq"), ("action", "addincart"), ("restext", "Added!")])), ("datas", cod([("datetime", inp["dishinfo"]["datetime"]), ("lord", inp["dishinfo"]["lord"]), ("dishid", inp["dishinfo"]["id"])]))]))));
    outpvar.open(htmlnode("p", extentattrs("Add + ")));
    outpvar.close();
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_l_otp_button(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("button", extentattrs(cod([("class", "btn waves-effect waves-light"), ("attr", cod([("type", "button")])), ("data", cod([("onclick", "sreq"), ("action", "sendotp"), ("fobj", "$(obj).parent().parent()[0]"), ("restext", "Re-send")]))]))));
  outpvar.open(htmlnode("p", extentattrs("Send OTP")));
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_loginmodal(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("attr", cod([("id", "loginmodal")])), ("class", "modal")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "modal-content container-fluid")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("ul", extentattrs(cod([("class", "tabs")]))));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("liclass", "tab col l6"), ("tablink", ["#logintab", "#signuptab"]), ("tabname", ["Login", "Signup"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("attr", cod([("id", "logintab")]))]))));
  outpvar.open(htmlnode("form", extentattrs(cod([("data", cod([("onsubmit", "sreq"), ("bobj", ""), ("action", "login"), ("res", "ms.reload();"), ("errorh", "error_login")]))]))));
  outpvar.cur.addfcdata("errorbox");
  outpvar.addchilds(newtag_errorbox(cod([]), ginp, outpvar.cur.fcalldata["errorbox"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.cur.addfcdata("input1");
  outpvar.addchilds(newtag_input1(cod([("label", "Phone number"), ("icon", "phone"), ("aclass", "col s12 l7 m6"), ("id", "loginphone"), ("dc", "phone")]), ginp, outpvar.cur.fcalldata["input1"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l4 m6")]))));
  outpvar.cur.addfcdata("l_otp_button");
  outpvar.addchilds(newtag_l_otp_button(cod([]), ginp, outpvar.cur.fcalldata["l_otp_button"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.cur.addfcdata("input1");
  outpvar.addchilds(newtag_input1(cod([("label", "Password or OTP"), ("icon", "vpn_key"), ("aclass", "col s12 l12 m12"), ("id", "loginpass"), ("type", "password"), ("dc", "password1")]), ginp, outpvar.cur.fcalldata["input1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col")]))));
  outpvar.open(htmlnode("button", extentattrs(cod([("class", "btn waves-effect waves-light"), ("attr", cod([("type", "submit")]))]))));
  outpvar.open(htmlnode("p", extentattrs("Login")));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("attr", cod([("id", "signuptab")]))]))));
  outpvar.open(htmlnode("form", extentattrs(cod([("data", cod([("onsubmit", "sreq"), ("bobj", ""), ("action", "signup"), ("res", "ms.reload();"), ("errorh", "error_login")]))]))));
  outpvar.cur.addfcdata("errorbox");
  outpvar.addchilds(newtag_errorbox(cod([]), ginp, outpvar.cur.fcalldata["errorbox"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.cur.addfcdata("input1");
  outpvar.addchilds(newtag_input1(cod([("label", "Phone number"), ("icon", "phone"), ("aclass", "col s12 l7 m6"), ("id", "signupphone"), ("dc", "phone")]), ginp, outpvar.cur.fcalldata["input1"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l4 m6")]))));
  outpvar.cur.addfcdata("l_otp_button");
  outpvar.addchilds(newtag_l_otp_button(cod([]), ginp, outpvar.cur.fcalldata["l_otp_button"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.cur.addfcdata("input1");
  outpvar.addchilds(newtag_input1(cod([("label", "Choose Password"), ("icon", "vpn_key"), ("aclass", "col s12 l6 m6"), ("id", "signuppass"), ("type", "password"), ("dc", "password1")]), ginp, outpvar.cur.fcalldata["input1"].root.content).root.content);
  outpvar.cur.addfcdata("input1");
  outpvar.addchilds(newtag_input1(cod([("label", "OTP"), ("icon", "vpn_key"), ("aclass", "col s12 l6 m6"), ("id", "signupotp"), ("type", "password"), ("dc", "otp")]), ginp, outpvar.cur.fcalldata["input1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.cur.addfcdata("input1");
  outpvar.addchilds(newtag_input1(cod([("label", "Name"), ("icon", "account_circle"), ("aclass", "col s12 l12 m12"), ("id", "signupname")]), ginp, outpvar.cur.fcalldata["input1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col")]))));
  outpvar.open(htmlnode("button", extentattrs(cod([("class", "btn waves-effect waves-light"), ("attr", cod([("type", "submit")]))]))));
  outpvar.open(htmlnode("p", extentattrs("Signup")));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_table1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("rows", []), ("thead", [])])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("table", extentattrs(cod([("class", inp["class"])]))));
  outpvar.open(htmlnode("thead", extentattrs(cod([]))));
  for i in forlist(inp["thead"], False ) :
    outpvar.open(htmlnode("th", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(i)));
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("tbody", extentattrs(cod([]))));
  for ii in forlist(inp["rows"], True ) :
    i = inp["rows"][ii];
    outpvar.open(htmlnode("tr", extentattrs(cod([]))));
    for jj in forlist(i, True ) :
      j = i[jj];
      outpvar.open(htmlnode("td", extentattrs(cod([]))));
      outpvar.open(htmlnode("p", extentattrs(j)));
      outpvar.close();
      outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_profilea1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("name", inp["name"]), ("href", myadd(myadd(inp["BASE"], "profile?uid="), inp["uid"]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  return outpvar;
  
def newtag_account_admin(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("attr", cod([("align", "center")]))]))));
  outpvar.cur.addfcdata("height");
  outpvar.addchilds(newtag_height(cod([("val", 20)]), ginp, outpvar.cur.fcalldata["height"].root.content).root.content);
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv(cod([("name", "Hey Admin,\n you are welcome"), ("font", "20px")]), ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.cur.addfcdata("height");
  outpvar.addchilds(newtag_height(cod([("val", 50)]), ginp, outpvar.cur.fcalldata["height"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("table", extentattrs(cod([("class", "bordered striped centered highlight")]))));
  outpvar.open(htmlnode("thead", extentattrs(cod([]))));
  for i in forlist(["UserID", "Name", "Email", "Phone", "User Type"], False ) :
    outpvar.open(htmlnode("th", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(i)));
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("tbody", extentattrs(cod([]))));
  for ii in forlist(inp["users"], True ) :
    i = inp["users"][ii];
    outpvar.open(htmlnode("tr", extentattrs(cod([]))));
    for jj in forlist(["id", "name", "email", "phone", "typetext"], True ) :
      jjj = ["id", "name", "email", "phone", "typetext"][jj];
      inp["j"] = i[jjj];
      outpvar.open(htmlnode("td", extentattrs(cod([]))));
      if (int((int((jjj == "name")) and int((i["type"] == "c"))))): 
        outpvar.cur.addfcdata("profilea1");
        outpvar.addchilds(newtag_profilea1(cod([("name", inp["j"]), ("uid", i["id"])]), ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
      elif (1): 
        outpvar.open(htmlnode("p", extentattrs(inp["j"])));
        outpvar.close();
      outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.cur.addfcdata("button1");
    outpvar.addchilds(newtag_button1(cod([("name", ("UnBlock" if (i["conf"]) else "Block")), ("datas", cod([("uid", i["id"]), ("isblock", int((i["conf"] != None)))])), ("data", cod([("onclick", "sreq"), ("action", "blockunblock"), ("restext", "Done!")]))]), ginp, outpvar.cur.fcalldata["button1"].root.content).root.content);
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_profile_chef_top2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row valign-wrapper")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l3"), ("attr", cod([("align", "center")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([]))));
  outpvar.cur.addfcdata("circleimg");
  outpvar.addchilds(newtag_circleimg(cod([("src", inp["uinfo"]["profilepic"])]), ginp, outpvar.cur.fcalldata["circleimg"].root.content).root.content);
  outpvar.close();
  if (inp["canedit"]): 
    outpvar.open(htmlnode("form", extentattrs(cod([("attr", cod([("enctype", "multipart/form-data"), ("method", "post")]))]))));
    outpvar.cur.addfcdata("a1");
    outpvar.addchilds(newtag_a1(cod([("name", "Upload Profile Pic"), ("attr", cod([("onclick", "uploadfile(this, \"profilepic\");")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
    outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([]))));
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv(cod([("name", myadd("Chef ", inp["uinfo"]["name"])), ("font", "25px"), ("fontw", "500")]), ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l6")]))));
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv(cod([("name", 38456), ("fontw", 600)]), ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv(cod([("name", "Dished Delivered")]), ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l6")]))));
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv(cod([("name", 56), ("fontw", 600)]), ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv(cod([("name", "People reviewed")]), ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l8 offset-l1")]))));
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv(cod([("font", "25px"), ("name", myadd("About ", inp["uinfo"]["name"])), ("fontw", 600)]), ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  if (inp["canedit"]): 
    outpvar.cur.addfcdata("a1");
    outpvar.addchilds(newtag_a1(cod([("name", "Edit"), ("attr", cod([("onclick", "ms.showtextarea(this);")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
    outpvar.open(htmlnode("div", extentattrs(cod([("class", "edittext"), ("style", cod([("display", "none")]))]))));
    outpvar.open(htmlnode("form", extentattrs(cod([("data", cod([("onsubmit", "sreq"), ("bobj", ""), ("action", "saveaboutinfo"), ("res", "ms.reload();")]))]))));
    outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("type", "hidden"), ("name", "chefid"), ("value", inp["uid"])]))]))));
    outpvar.open(htmlnode("textarea", extentattrs(cod([("attr", cod([("name", "aboutus")])), ("class", "materialize-textarea")]))));
    outpvar.open(htmlnode("p", extentattrs(convchars(inp["uinfo"]["aboutus"]))));
    outpvar.close();
    outpvar.close();
    outpvar.cur.addfcdata("button1");
    outpvar.addchilds(newtag_button1(cod([("name", "Save"), ("attr", cod([("type", "submit")]))]), ginp, outpvar.cur.fcalldata["button1"].root.content).root.content);
    outpvar.close();
    outpvar.close();
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv(cod([("font", "16px"), ("name", convchars(inp["uinfo"]["aboutus"]))]), ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs(cod([]))));
  outpvar.open(htmlnode("b", extentattrs(cod([]))));
  outpvar.open(htmlnode("p", extentattrs("Address: ")));
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("p", extentattrs(inp["uinfo"]["address"])));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_profile_chef(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "container-fluid")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l10 offset-l1 s10 m10 offset-s1 offset-m1")]))));
  outpvar.cur.addfcdata("profile_chef_top2");
  outpvar.addchilds(newtag_profile_chef_top2(cod([]), ginp, outpvar.cur.fcalldata["profile_chef_top2"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "msdivider")]))));
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "container-fluid")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.close();
  outpvar.close();
  if (inp["canedit"]): 
    outpvar.open(htmlnode("div", extentattrs(cod([("class", "container-fluid")]))));
    outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
    outpvar.open(htmlnode("div", extentattrs(cod([]))));
    outpvar.open(htmlnode("ul", extentattrs(cod([("class", "tabs")]))));
    outpvar.cur.addfcdata("disptabs");
    outpvar.addchilds(newtag_disptabs(cod([("liclass", "tab col s2"), ("tabname", myadd(["All Dishes"], inp["day5times"]["textl"])), ("tablink", myadd(["#alldishes"], inp["day5times"]["tabkeys1"]))]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("div", extentattrs(cod([("class", "")]))));
    outpvar.open(htmlnode("div", extentattrs(cod([("attr", cod([("id", "alldishes")]))]))));
    outpvar.cur.addfcdata("height");
    outpvar.addchilds(newtag_height(cod([("val", 20)]), ginp, outpvar.cur.fcalldata["height"].root.content).root.content);
    if (int((inp["viewtype"] == "a"))): 
      outpvar.cur.addfcdata("button1");
      outpvar.addchilds(newtag_button1(cod([("name", "Add a New Dish"), ("data", cod([("onclick", "slideform")]))]), ginp, outpvar.cur.fcalldata["button1"].root.content).root.content);
      outpvar.open(htmlnode("form", extentattrs(cod([("style", cod([("display", "none")])), ("attr", cod([("enctype", "multipart/form-data"), ("method", "post")]))]))));
      outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
      outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("type", "hidden"), ("name", "cid"), ("value", inp["uid"])]))]))));
      outpvar.cur.addfcdata("input2");
      outpvar.addchilds(newtag_input2(cod([("label", "Title of Dish"), ("aclass", "col s12 l6 m6"), ("id", "dishtitle")]), ginp, outpvar.cur.fcalldata["input2"].root.content).root.content);
      outpvar.cur.addfcdata("input2");
      outpvar.addchilds(newtag_input2(cod([("label", "Price of Dish"), ("aclass", "col s12 l6 m6"), ("id", "dishprice")]), ginp, outpvar.cur.fcalldata["input2"].root.content).root.content);
      outpvar.close();
      outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
      outpvar.open(htmlnode("textarea", extentattrs(cod([("class", "materialize-textarea"), ("attr", cod([("name", "descp"), ("placeholder", "Dish Description")]))]))));
      outpvar.close();
      outpvar.close();
      outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
      outpvar.open(htmlnode("div", extentattrs(cod([("class", "file-field input-field")]))));
      outpvar.open(htmlnode("div", extentattrs(cod([("class", "btn")]))));
      outpvar.open(htmlnode("span", extentattrs(cod([]))));
      outpvar.open(htmlnode("p", extentattrs("Upload Image")));
      outpvar.close();
      outpvar.close();
      outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("type", "file"), ("name", "dishpic")]))]))));
      outpvar.close();
      outpvar.open(htmlnode("div", extentattrs(cod([("class", "file-path-wrapper")]))));
      outpvar.open(htmlnode("input", extentattrs(cod([("class", "file-path-validate"), ("attr", cod([("type", "text")]))]))));
      outpvar.close();
      outpvar.close();
      outpvar.close();
      outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
      outpvar.open(htmlnode("div", extentattrs(cod([("class", "col")]))));
      outpvar.open(htmlnode("button", extentattrs(cod([("class", "btn waves-effect waves-light"), ("attr", cod([("type", "submit"), ("name", "adddish")]))]))));
      outpvar.open(htmlnode("p", extentattrs("Add")));
      outpvar.close();
      outpvar.close();
      outpvar.close();
      outpvar.close();
      outpvar.close();
    outpvar.open(htmlnode("div", extentattrs(cod([("class", "row"), ("attr", cod([("align", "center")]))]))));
    for i in forlist(inp["dispdata"], False ) :
      outpvar.cur.addfcdata("dispfood");
      outpvar.addchilds(newtag_dispfood(cod([("dishinfo", i)]), ginp, outpvar.cur.fcalldata["dispfood"].root.content).root.content);
    outpvar.close();
    outpvar.close();
    for ii in forlist(inp["day5times"]["tabkeys"], True ) :
      i = inp["day5times"]["tabkeys"][ii];
      outpvar.open(htmlnode("div", extentattrs(cod([("attr", cod([("id", i)]))]))));
      outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
      outpvar.open(htmlnode("table", extentattrs(cod([("class", "bordered")]))));
      outpvar.open(htmlnode("thead", extentattrs(cod([]))));
      for j in forlist(["Title", "Price", "Booked For Lunch", "Booked for Dinner"], False ) :
        outpvar.open(htmlnode("th", extentattrs(cod([]))));
        outpvar.open(htmlnode("p", extentattrs(j)));
        outpvar.close();
        outpvar.close();
      outpvar.close();
      for jj in forlist(inp["dispdata"], True ) :
        j = inp["dispdata"][jj];
        outpvar.open(htmlnode("tr", extentattrs(cod([]))));
        outpvar.open(htmlnode("th", extentattrs(cod([]))));
        outpvar.open(htmlnode("p", extentattrs(convchars(myadd(j["title"], "")))));
        outpvar.close();
        outpvar.close();
        outpvar.open(htmlnode("th", extentattrs(cod([]))));
        outpvar.open(htmlnode("p", extentattrs(j["price"])));
        outpvar.close();
        outpvar.close();
        outpvar.open(htmlnode("th", extentattrs(cod([]))));
        outpvar.cur.addfcdata("input1");
        outpvar.addchilds(newtag_input1(cod([("label", myadd(myadd("Plate Limit (", j[myadd("ollimit", ii)]), " Booked)")), ("id", myadd(myadd(myadd("lunch_", jj), "_"), ii)), ("data", cod([("dishid", j["id"]), ("day", ii)])), ("iclass", "numplatelimit"), ("value", j[myadd("llimit", ii)])]), ginp, outpvar.cur.fcalldata["input1"].root.content).root.content);
        outpvar.close();
        outpvar.open(htmlnode("th", extentattrs(cod([]))));
        outpvar.cur.addfcdata("input1");
        outpvar.addchilds(newtag_input1(cod([("label", myadd(myadd("Plate Limit (", j[myadd("odlimit", ii)]), " Booked)")), ("id", myadd(myadd(myadd("dinner_", jj), "_"), ii)), ("data", cod([("dishid", j["id"]), ("day", ii)])), ("iclass", "numplatelimit"), ("value", j[myadd("dlimit", ii)])]), ginp, outpvar.cur.fcalldata["input1"].root.content).root.content);
        outpvar.close();
        outpvar.close();
      outpvar.close();
      outpvar.open(htmlnode("div", extentattrs(cod([]))));
      if (int((len(inp["dispdata"]) != 0))): 
        outpvar.cur.addfcdata("button1");
        outpvar.addchilds(newtag_button1(cod([("name", "Save"), ("data", cod([("action", "savedaymenu"), ("onclick", "sreq"), ("params", myadd(myadd("ms.getnumlimit(", ii), ")"))])), ("datas", cod([("datetime", inp["day5times"]["timel"][ii]), ("cid", inp["uid"])]))]), ginp, outpvar.cur.fcalldata["button1"].root.content).root.content);
      outpvar.close();
      outpvar.close();
      outpvar.close();
    outpvar.close();
    outpvar.close();
    outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("attr", cod([("align", "center")])), ("style", cod([("margin", "20px")]))]))));
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv(cod([("name", "Dishes Serving today"), ("font", "25px")]), ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row"), ("attr", cod([("align", "center")]))]))));
  for i in forlist(inp["dispdata"], False ) :
    if (int((int((i["llimit0"] > 0)) or int((i["dlimit0"] > 0))))): 
      outpvar.cur.addfcdata("dispfood");
      outpvar.addchilds(newtag_dispfood(cod([("dishinfo", i)]), ginp, outpvar.cur.fcalldata["dispfood"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_select1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tlist", []), ("class", "browser-default"), ("aclass", "")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("select", extentattrs(cod([("class", myadd(myadd(inp["class"], " "), inp["aclass"])), ("name", inp["name"]), ("attr", inp["attr"])]))));
  if (int((inp["toptext"] != None))): 
    outpvar.open(htmlnode("option", extentattrs(cod([("attr", cod([("value", "")]))]))));
    outpvar.open(htmlnode("p", extentattrs(inp["toptext"])));
    outpvar.close();
    outpvar.close();
  for ii in forlist(inp["tlist"], True ) :
    i = inp["tlist"][ii];
    inp["attrs"] = cod([]);
    if (int((inp["vlist"] != None))): 
      inp["attrs"]["value"] = inp["vlist"][ii];
    elif (1): 
      inp["attrs"]["value"] = myadd(ii, 1);
    if (int((inp["selected"] == ii))): 
      inp["attrs"]["selected"] = "";
    outpvar.open(htmlnode("option", extentattrs(cod([("attr", inp["attrs"])]))));
    outpvar.open(htmlnode("p", extentattrs(i)));
    outpvar.close();
    outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_select2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tlist", []), ("dclass", "col l3 s12 m6"), ("class", "browser-default")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", inp["dclass"])]))));
  outpvar.cur.addfcdata("select1");
  outpvar.addchilds(newtag_select1(cod([("class", inp["class"]), ("tlist", inp["tlist"]), ("vlist", inp["vlist"]), ("toptext", inp["toptext"]), ("selected", inp["selected"])]), ginp, outpvar.cur.fcalldata["select1"].root.content).root.content);
  outpvar.close();
  return outpvar;
  
def newtag_mselect(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tlist", [])])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  for ii in forlist(inp["tlist"], True ) :
    i = inp["tlist"][ii];
    inp["attrs"] = cod([]);
    if (int((inp["vlist"] != None))): 
      inp["attrs"]["value"] = inp["vlist"][ii];
    elif (1): 
      inp["attrs"]["value"] = myadd(ii, 1);
    if (int((inp["selected"] == ii))): 
      inp["attrs"]["selected"] = "";
    outpvar.cur.addfcdata("checkbox1");
    outpvar.addchilds(newtag_checkbox1(cod([("label", i), ("id", myadd(myadd(inp["id"], "_"), ii))]), ginp, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
  return outpvar;
  
def newtag_mselect1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tlist", [])])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("id", inp["id"]), ("class", "dropdown-content p5"), ("tlist", [])]))));
  outpvar.cur.addfcdata("mselect");
  outpvar.addchilds(newtag_mselect(cod([("vlist", inp["vlist"]), ("tlist", inp["tlist"]), ("id", inp["id"])]), ginp, outpvar.cur.fcalldata["mselect"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("a", extentattrs(cod([("class", "dropdown-button"), ("data", cod([("activates", inp["id"])]))]))));
  outpvar.open(htmlnode("p", extentattrs(inp["label"])));
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_mselect2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("class", "col l3 s12 m6")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", inp["class"])]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "mselect complexinput"), ("data", cod([("complexinput", "ci_checkbox")])), ("attr", cod([("name", inp["id"])]))]))));
  outpvar.cur.addfcdata("mselect1");
  outpvar.addchilds(newtag_mselect1(cod([("id", inp["id"]), ("tlist", inp["tlist"]), ("label", inp["label"]), ("selectall", inp["selectall"])]), ginp, outpvar.cur.fcalldata["mselect1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_switch1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("on", "Yes"), ("off", "No")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "switch")]))));
  outpvar.open(htmlnode("label", extentattrs(cod([]))));
  outpvar.open(htmlnode("p", extentattrs(inp["off"])));
  outpvar.close();
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("type", "checkbox"), ("name", inp["name"])]))]))));
  outpvar.open(htmlnode("span", extentattrs(cod([("class", "lever")]))));
  outpvar.close();
  outpvar.open(htmlnode("p", extentattrs(inp["on"])));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_switch2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("class", "col l3 s12 m6")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", inp["class"])]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "m5")]))));
  outpvar.open(htmlnode("p", extentattrs(inp["label"])));
  outpvar.close();
  outpvar.cur.addfcdata("switch1");
  outpvar.addchilds(newtag_switch1(cod([("name", inp["name"])]), ginp, outpvar.cur.fcalldata["switch1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_orderl_admin(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("table", extentattrs(cod([("class", "bordered")]))));
  outpvar.open(htmlnode("thead", extentattrs(cod([]))));
  for i in forlist(["Odered At", "Delivery Date", "Chef", "User", "Dish", "Price", "Chef Address", "User Address", "Status"], False ) :
    outpvar.open(htmlnode("th", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(i)));
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("tbody", extentattrs(cod([]))));
  for ii in forlist(inp["orderl"], True ) :
    i = inp["orderl"][ii];
    outpvar.open(htmlnode("tr", extentattrs(cod([("class", "cartitems"), ("datas", cod([("datetime", i["datetime"]), ("cid", i["cid"]), ("lord", i["lord"]), ("dishid", i["dishid"])]))]))));
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(i["timetext"])));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(i["datetimetext"])));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.cur.addfcdata("profilea1");
    outpvar.addchilds(newtag_profilea1(cod([("name", i["cname"]), ("uid", i["cid"])]), ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.cur.addfcdata("profilea1");
    outpvar.addchilds(newtag_profilea1(cod([("name", i["uname"]), ("uid", i["uid"])]), ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(i["title"])));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.cur.addfcdata("icon1");
    outpvar.addchilds(newtag_icon1(cod([("img", "photo/inr2.png")]), ginp, outpvar.cur.fcalldata["icon1"].root.content).root.content);
    outpvar.open(htmlnode("span", extentattrs(cod([("class", "itemprice")]))));
    outpvar.open(htmlnode("p", extentattrs(myadd(myadd(myadd(myadd(i["price"], "*"), i["numplate"]), "="), (i["price"] * i["numplate"])))));
    outpvar.close();
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(myadd(myadd(myadd(myadd(myadd("(", i["clat"]), ", "), i["clng"]), ")<br>"), i["caddress"]))));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(myadd(myadd(myadd(myadd(myadd("(", i["lat"]), ", "), i["lng"]), ")<br>"), i["uaddress"]))));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(i["status"])));
    outpvar.close();
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_orderl_user(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("table", extentattrs(cod([("class", "bordered")]))));
  outpvar.open(htmlnode("thead", extentattrs(cod([]))));
  for i in forlist(["Odered At", "Delivery Date", "Chef", "Dish", "Price", "User Address", "Status"], False ) :
    outpvar.open(htmlnode("th", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(i)));
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("tbody", extentattrs(cod([]))));
  for ii in forlist(inp["orderl"], True ) :
    i = inp["orderl"][ii];
    outpvar.open(htmlnode("tr", extentattrs(cod([("class", "cartitems"), ("datas", cod([("datetime", i["datetime"]), ("cid", i["cid"]), ("lord", i["lord"]), ("dishid", i["dishid"])]))]))));
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(i["timetext"])));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(i["datetimetext"])));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.cur.addfcdata("profilea1");
    outpvar.addchilds(newtag_profilea1(cod([("name", i["cname"]), ("uid", i["cid"])]), ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(i["title"])));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.cur.addfcdata("icon1");
    outpvar.addchilds(newtag_icon1(cod([("img", "photo/inr2.png")]), ginp, outpvar.cur.fcalldata["icon1"].root.content).root.content);
    outpvar.open(htmlnode("span", extentattrs(cod([("class", "itemprice")]))));
    outpvar.open(htmlnode("p", extentattrs(myadd(myadd(myadd(myadd(i["price"], "*"), i["numplate"]), "="), (i["price"] * i["numplate"])))));
    outpvar.close();
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(myadd(myadd(myadd(myadd(myadd("(", i["lat"]), ", "), i["lng"]), ")<br>"), i["uaddress"]))));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(i["status"])));
    outpvar.close();
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_orderl_chef(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("table", extentattrs(cod([("class", "bordered")]))));
  outpvar.open(htmlnode("thead", extentattrs(cod([]))));
  for i in forlist(["Odered At", "Delivery Date", "User", "Dish", "Price", "User Address", "Status"], False ) :
    outpvar.open(htmlnode("th", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(i)));
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("tbody", extentattrs(cod([]))));
  for ii in forlist(inp["orderl"], True ) :
    i = inp["orderl"][ii];
    outpvar.open(htmlnode("tr", extentattrs(cod([("class", "cartitems"), ("datas", cod([("datetime", i["datetime"]), ("cid", i["cid"]), ("lord", i["lord"]), ("dishid", i["dishid"])]))]))));
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(i["timetext"])));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(i["datetimetext"])));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.cur.addfcdata("profilea1");
    outpvar.addchilds(newtag_profilea1(cod([("name", i["cname"]), ("uid", i["cid"])]), ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.cur.addfcdata("profilea1");
    outpvar.addchilds(newtag_profilea1(cod([("name", i["uname"]), ("uid", i["uid"])]), ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(i["title"])));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.cur.addfcdata("icon1");
    outpvar.addchilds(newtag_icon1(cod([("img", "photo/inr2.png")]), ginp, outpvar.cur.fcalldata["icon1"].root.content).root.content);
    outpvar.open(htmlnode("span", extentattrs(cod([("class", "itemprice")]))));
    outpvar.open(htmlnode("p", extentattrs(myadd(myadd(myadd(myadd(i["price"], "*"), i["numplate"]), "="), (i["price"] * i["numplate"])))));
    outpvar.close();
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(myadd(myadd(myadd(myadd(myadd("(", i["clat"]), ", "), i["clng"]), ")<br>"), i["caddress"]))));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(myadd(myadd(myadd(myadd(myadd("(", i["lat"]), ", "), i["lng"]), ")<br>"), i["uaddress"]))));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.open(htmlnode("p", extentattrs(i["status"])));
    outpvar.close();
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_orderl(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("utype", ginp["islogin"])])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  if (int((inp["utype"] == "u"))): 
    outpvar.cur.addfcdata("orderl_user");
    outpvar.addchilds(newtag_orderl_user(cod([("orderl", inp["orderl"])]), ginp, outpvar.cur.fcalldata["orderl_user"].root.content).root.content);
  if (int((inp["utype"] == "c"))): 
    outpvar.cur.addfcdata("orderl_chef");
    outpvar.addchilds(newtag_orderl_chef(cod([("orderl", inp["orderl"])]), ginp, outpvar.cur.fcalldata["orderl_chef"].root.content).root.content);
  if (int((inp["utype"] == "a"))): 
    outpvar.cur.addfcdata("orderl_admin");
    outpvar.addchilds(newtag_orderl_admin(cod([("orderl", inp["orderl"])]), ginp, outpvar.cur.fcalldata["orderl_admin"].root.content).root.content);
  return outpvar;
  
def newtag_errorbox(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row hiddenerror")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s12 l12")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "card-panel red white-text center errortext")]))));
  outpvar.open(htmlnode("p", extentattrs("")));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_menu_nofood(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l12 m12 s12")]))));
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv(cod([("name", "No chef is serving in this location. We are trying hard to serve you in this location, will let you know once this location is launched"), ("font", "20px")]), ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.close();
  return outpvar;
  
def newtag_kurry_footer(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "page-footer darken-4"), ("style", cod([("margin-bottom", "0px"), ("padding-bottom", "0px")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "container")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row"), ("style", cod([("margin-bottom", "-25px")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s2 m2 l3 offset-l2 offset-m2")]))));
  outpvar.open(htmlnode("h5", extentattrs(cod([]))));
  outpvar.open(htmlnode("p", extentattrs("Social Media")));
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([]))));
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("name", "Facebook")]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("name", "Twitter")]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("name", "Instagram")]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s2 m2 l3")]))));
  outpvar.open(htmlnode("h5", extentattrs(cod([]))));
  outpvar.open(htmlnode("p", extentattrs("Help")));
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([]))));
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("name", "About us"), ("attr", cod([("onclick", "$(\"#aboutus\").openModal();")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("name", "Contact us"), ("attr", cod([("onclick", "$(\"#contactusform\").openModal();")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s2 m2 l3")]))));
  outpvar.open(htmlnode("h5", extentattrs(cod([]))));
  outpvar.open(htmlnode("p", extentattrs("Legal")));
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([]))));
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("name", "Company Policies, Terms and Conditions"), ("attr", cod([("onclick", "$(\"#policy\").openModal();")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l12 center ")]))));
  outpvar.open(htmlnode("p", extentattrs("&copy; Copyright 2015 KurryBox")));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_kurry_contactus_form(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s12 l12 m12")]))));
  outpvar.open(htmlnode("h3", extentattrs(cod([("class", "grey-text text-darken-4")]))));
  outpvar.open(htmlnode("p", extentattrs("Contact US")));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s12 l6 m6")]))));
  outpvar.open(htmlnode("h5", extentattrs(cod([("class", "grey-text text-darken-2")]))));
  outpvar.open(htmlnode("p", extentattrs("Mail")));
  outpvar.close();
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon(cod([("name", "mail"), ("aclass", "tiny")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "grey-text")]))));
  outpvar.open(htmlnode("p", extentattrs("ContactUs@kurrybox.in")));
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("h5", extentattrs(cod([("class", "grey-text text-darken-2")]))));
  outpvar.open(htmlnode("p", extentattrs("Call")));
  outpvar.close();
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon(cod([("name", "call"), ("aclass", "tiny")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "grey-text")]))));
  outpvar.open(htmlnode("p", extentattrs("+91 704 211 4473")));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_kurry_aboutus(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "card-content")]))));
  outpvar.open(htmlnode("h3", extentattrs(cod([("class", "card-title")]))));
  outpvar.open(htmlnode("p", extentattrs("About Us")));
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([]))));
  outpvar.open(htmlnode("p", extentattrs(inp["aboutus_content"])));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_kurry_policy(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "card-content")]))));
  outpvar.open(htmlnode("h3", extentattrs(cod([("class", "card-title")]))));
  outpvar.open(htmlnode("p", extentattrs("Policy")));
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([]))));
  outpvar.open(htmlnode("p", extentattrs(inp["policy_content"])));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_cp_contactus_form(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s12 l12 m12")]))));
  outpvar.open(htmlnode("h3", extentattrs(cod([("class", "grey-text text-darken-4")]))));
  outpvar.addtext("Contact US");
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s12 l6 m6")]))));
  outpvar.open(htmlnode("h5", extentattrs(cod([("class", "grey-text text-darken-2")]))));
  outpvar.addtext("Address");
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon(cod([("name", "navigation"), ("aclass", "tiny")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "grey-text")]))));
  outpvar.addtext("58/1 2nd Floor,<br> Kalu Sarai<br>  Near Hauz Khas Metro Station<br> New Delhi - 110016<br>India");
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s12 l6 m6")]))));
  outpvar.open(htmlnode("h5", extentattrs(cod([("class", "grey-text text-darken-2")]))));
  outpvar.addtext("Mail");
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon(cod([("name", "mail"), ("aclass", "tiny")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "grey-text")]))));
  outpvar.addtext("mohitsaini1196@gmail.com");
  outpvar.close();
  outpvar.open(htmlnode("h5", extentattrs(cod([("class", "grey-text text-darken-2")]))));
  outpvar.addtext("Call");
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon(cod([("name", "call"), ("aclass", "tiny")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "grey-text")]))));
  outpvar.addtext("+91 750 375 9053");
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_cp_our_story(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "card-content")]))));
  outpvar.open(htmlnode("h3", extentattrs(cod([("class", "card-title")]))));
  outpvar.addtext("Our Story");
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([]))));
  outpvar.addtext(inp["our_story_content"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_headertabs_cp(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("text", "MyFav"), ("attr", cod([("onclick", "$(\"#myfavlist\").openModal();")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("text", "Contact Us"), ("attr", cod([("onclick", "$(\"#contactusform\").openModal();")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("text", "Our Story"), ("attr", cod([("onclick", "$(\"#ourstory\").openModal();")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("text", "Provider Form"), ("attr", cod([("onclick", "$(\"#providerform\").openModal();")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  return outpvar;
  
def newtag_cp_filterform(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l11 s11 m11"), ("id", "mainfilter")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("padding", "8px"), ("margin-bottom", "4px")])), ("class", "card-panel")]))));
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("placeholder", "Search Location"), ("autofocus", "true")])), ("class", "inputplaceholder mainsearch"), ("style", cod([("border-radius", "0px"), ("border", "solid black 0px"), ("font-size", "13px")])), ("id", "searchloc")]))));
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("margin-top", "0px"), ("padding", "8px"), ("margin-bottom", "-5px")])), ("class", "card-panel")]))));
  outpvar.open(htmlnode("form", extentattrs(cod([("data", cod([("onsubmit", "sreq"), ("bobj", ""), ("action", "search"), ("res", "draw_points(data.data);")]))]))));
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("placeholder", "Search keywords"), ("name", "keyw")])), ("class", "inputplaceholder mainsearch"), ("style", cod([("border-radius", "0px"), ("border", "solid black 0px"), ("font-size", "13px")]))]))));
  outpvar.open(htmlnode("button", extentattrs(cod([("attr", cod([("type", "submit")])), ("style", cod([("display", "none")]))]))));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  if (1): 
    outpvar.open(htmlnode("ul", extentattrs(cod([("class", "collapsible"), ("attr", cod([("data-collapsible", "accordion")]))]))));
    for ii in forlist(inp["catg"], True ) :
      i = inp["catg"][ii];
      outpvar.open(htmlnode("li", extentattrs(cod([]))));
      outpvar.open(htmlnode("div", extentattrs(cod([("class", "collapsible-header")]))));
      outpvar.cur.addfcdata("icon1");
      outpvar.addchilds(newtag_icon1(cod([("img", i["icon"])]), ginp, outpvar.cur.fcalldata["icon1"].root.content).root.content);
      outpvar.addtext(i["name"]);
      outpvar.close();
      outpvar.open(htmlnode("div", extentattrs(cod([("class", "collapsible-body")]))));
      outpvar.open(htmlnode("div", extentattrs(cod([("class", "subcats1"), ("style", cod([("padding", "5px"), ("padding-left", "20px"), ("padding-bottom", "0px"), ("padding-top", "0px")]))]))));
      outpvar.open(htmlnode("ul", extentattrs(cod([("class", "collapsible_sub"), ("attr", cod([("data-collapsible", "accordion")]))]))));
      for jj in forlist(i["child"], True ) :
        j = i["child"][jj];
        outpvar.open(htmlnode("li", extentattrs(cod([("class", "")]))));
        outpvar.open(htmlnode("div", extentattrs(cod([("class", "collapsible-header"), ("style", cod([("border-bottom", "solid black 0px"), ("border-top", "1px solid #DDD")]))]))));
        outpvar.addtext(j["name"]);
        outpvar.close();
        outpvar.open(htmlnode("div", extentattrs(cod([("class", "collapsible-body")]))));
        outpvar.open(htmlnode("div", extentattrs(cod([("class", "subcats2"), ("style", cod([("padding-left", "30px")]))]))));
        outpvar.open(htmlnode("ul", extentattrs(cod([]))));
        outpvar.open(htmlnode("li", extentattrs(cod([]))));
        outpvar.open(htmlnode("div", extentattrs(cod([]))));
        outpvar.cur.addfcdata("checkbox1");
        outpvar.addchilds(newtag_checkbox1(cod([("label", "Select All"), ("id", myadd(myadd(myadd(myadd(myadd("catsubcat", ii), "_"), jj), "_"), "selectall")), ("aclass", "selectall"), ("data", cod([("onclick", "selectall redraw"), ("catgtid", myadd(myadd(i["id"], "_"), j["id"]))])), ("labels", cod([("font-size", "12px")]))]), ginp, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
        outpvar.close();
        outpvar.close();
        for kk in forlist(j["child"], True ) :
          k = j["child"][kk];
          outpvar.open(htmlnode("li", extentattrs(cod([]))));
          outpvar.open(htmlnode("div", extentattrs(cod([]))));
          outpvar.cur.addfcdata("checkbox1");
          outpvar.addchilds(newtag_checkbox1(cod([("label", k["name"]), ("id", myadd(myadd(myadd(myadd(myadd("catsubcat", ii), "_"), jj), "_"), kk)), ("data", cod([("catgtid", myadd(myadd(myadd(myadd(i["id"], "_"), j["id"]), "_"), k["id"])), ("onclick", "redraw")])), ("labels", cod([("font-size", "12px")]))]), ginp, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
          outpvar.close();
          outpvar.close();
        outpvar.close();
        outpvar.close();
        outpvar.close();
        outpvar.close();
      outpvar.close();
      outpvar.close();
      outpvar.close();
      outpvar.close();
    outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("background-color", "white"), ("padding", "5px")]))]))));
    outpvar.cur.addfcdata("a1");
    outpvar.addchilds(newtag_a1(cod([("text", "See All Cats"), ("attr", cod([("onclick", "$(\"#commoncats\").openModal();")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l1 s1 m1")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("padding", "8px"), ("margin-bottom", "4px"), ("padding-left", "0px"), ("margin-left", "-20px")]))]))));
  outpvar.cur.addfcdata("icon1");
  outpvar.addchilds(newtag_icon1(cod([("img", "photo/minimize1.png"), ("class", "pointer"), ("attr", cod([("onclick", "minimaxifilter(1);")]))]), ginp, outpvar.cur.fcalldata["icon1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_cp_selectallcatgs(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s6 l6 m6")]))));
  outpvar.addtext("Select The Cats");
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s6 l6 m6")]))));
  outpvar.cur.addfcdata("button1");
  outpvar.addchilds(newtag_button1(cod([("name", "OK"), ("attr", cod([("onclick", " $(\"#commoncats\").closeModal();")]))]), ginp, outpvar.cur.fcalldata["button1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("ul", extentattrs(cod([("class", "tabs")]))));
  for ii in forlist(inp["catg"], True ) :
    i = inp["catg"][ii];
    outpvar.open(htmlnode("li", extentattrs(cod([("class", "tab col l4 m4 s4")]))));
    outpvar.cur.addfcdata("a1");
    outpvar.addchilds(newtag_a1(cod([("href", myadd("#modal", i["name"])), ("text", i["name"])]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
    outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  for ii in forlist(inp["catg"], True ) :
    i = inp["catg"][ii];
    outpvar.open(htmlnode("div", extentattrs(cod([("id", myadd("modal", i["name"])), ("class", "row")]))));
    for j in forlist(4, False ) :
      outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l3 m3 s6")]))));
      for kk in forlist(inp["commoncats"][ii][j], True ) :
        k = inp["commoncats"][ii][j][kk];
        outpvar.open(htmlnode("div", extentattrs(cod([]))));
        outpvar.cur.addfcdata("checkbox1");
        outpvar.addchilds(newtag_checkbox1(cod([("label", k[0]), ("id", myadd(myadd(myadd(myadd(myadd("commoncats_", ii), "_"), j), "_"), kk)), ("lstyle", cod([("color", "black"), ("font-size", "20px")])), ("data", cod([("onclick", "selectall")])), ("labels", cod([("color", "black")]))]), ginp, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
        outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("font-wight", 700), ("font-size", "18px")]))]))));
        outpvar.close();
        for ll in forlist(k, True ) :
          l = k[ll];
          if (int((ll != 0))): 
            outpvar.open(htmlnode("div", extentattrs(cod([]))));
            outpvar.cur.addfcdata("checkbox1");
            outpvar.addchilds(newtag_checkbox1(cod([("label", l), ("id", myadd(myadd(myadd(myadd(myadd(myadd(myadd("commoncats_", ii), "_"), j), "_"), kk), "_"), ll)), ("labels", cod([("font-size", "12px")]))]), ginp, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
            outpvar.close();
        outpvar.close();
      outpvar.close();
    outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_main1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("css", []), ("js", []), ("bodystyle", cod([])), ("htmlstyle", cod([])), ("title", "KurryBox")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  inp["js"] = myadd(["js/main.js"], inp["js"]);
  outpvar.cur.addfcdata("main");
  outpvar.cur.fcalldata["main"].addchilds(innerHTML);
  outpvar.addchilds(newtag_main(cod([("title", inp["title"]), ("css", inp["css"]), ("js", inp["js"]), ("bodystyle", inp["bodystyle"]), ("htmlstyle", inp["htmlstyle"])]), ginp, outpvar.cur.fcalldata["main"].root.content).root.content);
  return outpvar;
  
def newtag_main2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("css", []), ("js", []), ("bodystyle", cod([])), ("htmlstyle", cod([])), ("title", "KurryBox")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  inp["js"] = myadd(["js/main.js"], inp["js"]);
  outpvar.cur.addfcdata("main");
  outpvar.cur.fcalldata["main"].addchilds(innerHTML);
  outpvar.cur.fcalldata["main"].cur.addfcdata("loginmodal");
  outpvar.cur.fcalldata["main"].addchilds(newtag_loginmodal(cod([]), ginp, outpvar.cur.fcalldata["main"].cur.fcalldata["loginmodal"].root.content).root.content);
  outpvar.addchilds(newtag_main(cod([("title", inp["title"]), ("css", inp["css"]), ("js", inp["js"]), ("bodystyle", inp["bodystyle"]), ("htmlstyle", inp["htmlstyle"]), ("acss", ["css/materialize.min.css", "css/lib.css", "css/materialize.min.css", "css/custom-stylesheet.css", "css/jquery.bxslider.css", "mslib/css/gfont.css", "css/lib.css", "css/main.css", "css/style.css"])]), ginp, outpvar.cur.fcalldata["main"].root.content).root.content);
  return outpvar;
  
def newtag_bigsearch(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row"), ("style", cod([("background-color", "")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l1 m1")]))));
  outpvar.addtext("&nbsp;");
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col m8 s12 l9"), ("style", cod([("padding", "0px"), ("margin", "0px")]))]))));
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("placeholder", inp["ph"]), ("id", inp["id"]), ("autofocus", inp["autofocus"])])), ("class", "bigsearch definput"), ("style", cod([("border-radius", "0px")]))]))));
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col m2 s12 l1 "), ("style", cod([("padding", "0px"), ("margin", "0px")]))]))));
  outpvar.open(htmlnode("button", extentattrs(cod([("class", "bigsearchbutton waves-effect waves-light btn"), ("style", cod([("border-radius", "0px")])), ("attr", cod([("type", "submit")]))]))));
  outpvar.addtext("Go");
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon(cod([("name", "send"), ("aclass", "right")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_header2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tabname", []), ("tablink", []), ("tabname1", []), ("tablink1", [])])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "navbar-fixed ")]))));
  outpvar.open(htmlnode("nav", extentattrs(cod([("class", "white"), ("attr", cod([("role", "container")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "nav-wrapper container")]))));
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("id", "logo-container"), ("href", inp["HOST"])])), ("class", "brand-logo center")]))));
  outpvar.open(htmlnode("img", extentattrs(cod([("attr", cod([("src", "photo/logo4.png")])), ("class", "responsive-img"), ("style", cod([("vertical-align", "middle")]))]))));
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("class", "left hide-on-med-and-down")]))));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("tabname", inp["tabname1"]), ("tablink", inp["tablink1"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("class", "right hide-on-med-and-down")]))));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("tabname", inp["tabname"]), ("tablink", inp["tablink"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("href", "#loginmodal"), ("class", "modal-trigger"), ("text", "Login")]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("attr", cod([("id", "nav-mobile")])), ("class", "side-nav")]))));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("tabname", inp["tabname"]), ("tablink", inp["tablink"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("data-activates", "nav-mobile")])), ("class", "button-collapse")]))));
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon(cod([("name", "menu")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_header2_user(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tabname", []), ("tablink", []), ("tabname1", []), ("tablink1", [])])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "navbar-fixed ")]))));
  outpvar.open(htmlnode("ul", extentattrs(cod([("id", "dropdown1"), ("class", "dropdown-content")]))));
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("href", myadd(inp["BASE"], "account")), ("text", "Account")]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("href", myadd(inp["BASE"], "orders")), ("text", "Orders")]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("href", myadd(inp["HOST"], "?logout")), ("text", "Logout")]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("nav", extentattrs(cod([("class", "white"), ("attr", cod([("role", "container")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "nav-wrapper container")]))));
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("id", "logo-container"), ("href", inp["HOST"])])), ("class", "brand-logo center")]))));
  outpvar.open(htmlnode("img", extentattrs(cod([("attr", cod([("src", "photo/logo4.png")])), ("class", "responsive-img"), ("style", cod([("vertical-align", "middle")]))]))));
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("class", "left hide-on-med-and-down")]))));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("tabname", inp["tabname1"]), ("tablink", inp["tablink1"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("class", "right hide-on-med-and-down")]))));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("tabname", inp["tabname"]), ("tablink", inp["tablink"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("class", "dropdown-button"), ("text", myadd(myadd(("&nbsp;" * 5), inp["loginname"]), ("&nbsp;" * 10))), ("data", cod([("activates", "dropdown1")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("attr", cod([("id", "nav-mobile")])), ("class", "side-nav")]))));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("tabname", inp["tabname"]), ("tablink", inp["tablink"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("data-activates", "nav-mobile")])), ("class", "button-collapse")]))));
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon(cod([("name", "menu")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_header2_chef(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tabname", []), ("tablink", []), ("tabname1", []), ("tablink1", [])])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "navbar-fixed ")]))));
  outpvar.open(htmlnode("ul", extentattrs(cod([("id", "dropdown1"), ("class", "dropdown-content")]))));
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("href", myadd(inp["BASE"], "profile")), ("text", "Profile")]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("href", myadd(inp["BASE"], "orders")), ("text", "Orders")]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("href", myadd(inp["HOST"], "?logout")), ("text", "Logout")]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("nav", extentattrs(cod([("class", "white"), ("attr", cod([("role", "container")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "nav-wrapper container")]))));
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("id", "logo-container"), ("href", inp["HOST"])])), ("class", "brand-logo center")]))));
  outpvar.open(htmlnode("img", extentattrs(cod([("attr", cod([("src", "photo/logo4.png")])), ("class", "responsive-img"), ("style", cod([("vertical-align", "middle")]))]))));
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("class", "left hide-on-med-and-down")]))));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("tabname", inp["tabname1"]), ("tablink", inp["tablink1"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("class", "right hide-on-med-and-down")]))));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("tabname", inp["tabname"]), ("tablink", inp["tablink"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("class", "dropdown-button"), ("text", myadd(myadd(("&nbsp;" * 5), "Profile"), ("&nbsp;" * 10))), ("data", cod([("activates", "dropdown1")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("attr", cod([("id", "nav-mobile")])), ("class", "side-nav")]))));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("tabname", inp["tabname"]), ("tablink", inp["tablink"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("data-activates", "nav-mobile")])), ("class", "button-collapse")]))));
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon(cod([("name", "menu")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_header2_admin(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tabname", []), ("tablink", [])])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "navbar-fixed ")]))));
  outpvar.open(htmlnode("ul", extentattrs(cod([("id", "dropdown1"), ("class", "dropdown-content")]))));
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("href", myadd(inp["BASE"], "account")), ("text", "Account")]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("href", myadd(inp["BASE"], "orders")), ("text", "Orders")]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("href", myadd(inp["HOST"], "?logout")), ("text", "Logout")]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("nav", extentattrs(cod([("class", "white"), ("attr", cod([("role", "container")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "nav-wrapper container")]))));
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("id", "logo-container"), ("href", inp["HOST"])])), ("class", "brand-logo")]))));
  outpvar.open(htmlnode("img", extentattrs(cod([("attr", cod([("src", "photo/mylogo1.png")])), ("class", "circle responsive-img"), ("style", cod([("vertical-align", "middle")]))]))));
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("class", "right hide-on-med-and-down")]))));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("tabname", inp["tabname"]), ("tablink", inp["tablink"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("class", "dropdown-button"), ("text", myadd(myadd(("&nbsp;" * 5), "Profile"), ("&nbsp;" * 10))), ("data", cod([("activates", "dropdown1")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("attr", cod([("id", "nav-mobile")])), ("class", "side-nav")]))));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("tabname", inp["tabname"]), ("tablink", inp["tablink"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("data-activates", "nav-mobile")])), ("class", "button-collapse")]))));
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon(cod([("name", "menu")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_header4(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  if (int((inp["islogin"] == None))): 
    outpvar.cur.addfcdata("header2");
    outpvar.addchilds(newtag_header2(cod([("tablink", [myadd(inp["BASE"], "chefjoin")]), ("tabname", ["Be a Chef"]), ("tablink1", [""]), ("tabname1", ["Blog"])]), ginp, outpvar.cur.fcalldata["header2"].root.content).root.content);
  elif (int((inp["islogin"] == "u"))): 
    outpvar.cur.addfcdata("header2_user");
    outpvar.addchilds(newtag_header2_user(cod([("tablink", [inp["HOST"], "", "", myadd(inp["BASE"], "cart")]), ("tabname", ["Home", "Our Story", "Blog", "Cart"])]), ginp, outpvar.cur.fcalldata["header2_user"].root.content).root.content);
  elif (int((inp["islogin"] == "a"))): 
    outpvar.cur.addfcdata("header2_admin");
    outpvar.addchilds(newtag_header2_admin(cod([("tablink", [inp["HOST"], "", "", "", "", ""]), ("tabname", ["Home", "Our Story", "Blog"])]), ginp, outpvar.cur.fcalldata["header2_admin"].root.content).root.content);
  elif (int((inp["islogin"] == "c"))): 
    outpvar.cur.addfcdata("header2_chef");
    outpvar.addchilds(newtag_header2_chef(cod([("tablink", [inp["HOST"], "", "", "", "", ""]), ("tabname", ["Home", "Our Story", "Blog"])]), ginp, outpvar.cur.fcalldata["header2_chef"].root.content).root.content);
  return outpvar;
  
def newtag_header3(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tabname", []), ("tablink", [])])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "navbar-fixed ")]))));
  outpvar.open(htmlnode("nav", extentattrs(cod([("class", "white"), ("attr", cod([("role", "container")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "nav-wrapper container")]))));
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("id", "logo-container"), ("href", inp["BASE"])])), ("class", "brand-logo")]))));
  outpvar.open(htmlnode("img", extentattrs(cod([("attr", cod([("src", "photo/mylogo1.png")])), ("class", "circle responsive-img"), ("style", cod([("vertical-align", "middle")]))]))));
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("class", "right hide-on-med-and-down")]))));
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.open(htmlnode("a", extentattrs(cod([("class", "dropdown-button"), ("attr", cod([("data-activates", "dropdown2")]))]))));
  outpvar.addtext(myadd(myadd(("&nbsp;" * 10), "Today, 28th Oct"), ("&nbsp;" * 10)));
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.open(htmlnode("a", extentattrs(cod([("class", "dropdown-button"), ("attr", cod([("data-activates", "dropdown1")]))]))));
  outpvar.addtext(myadd(myadd(("&nbsp;" * 5), "All"), ("&nbsp;" * 20)));
  outpvar.close();
  outpvar.close();
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("tabname", inp["tabname"]), ("tablink", inp["tablink"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("attr", cod([("id", "dropdown1")])), ("class", "dropdown-content")]))));
  inp["foodtype"] = ["All", "Veg", "Non-Veg"];
  for ii in forlist(inp["foodtype"], True ) :
    i = inp["foodtype"][ii];
    outpvar.open(htmlnode("li", extentattrs(cod([]))));
    outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("href", "")]))]))));
    outpvar.addtext(i);
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("attr", cod([("id", "dropdown2")])), ("class", "dropdown-content")]))));
  inp["nextdays"] = ["Today, 26 Oct", "27 Oct", "28 Oct"];
  for ii in forlist(inp["nextdays"], True ) :
    i = inp["nextdays"][ii];
    outpvar.open(htmlnode("li", extentattrs(cod([]))));
    outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("href", "")]))]))));
    outpvar.addtext(i);
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_dispfood(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s12 l4 m6 "), ("style", cod([]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", " card-panel"), ("style", cod([("margin-bottom", "40px"), ("padding", "0px")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([]))));
  outpvar.cur.addfcdata("resimg");
  outpvar.addchilds(newtag_resimg(cod([("src", inp["dishinfo"]["pic"])]), ginp, outpvar.cur.fcalldata["resimg"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("padding-bottom", "10px")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("padding", "10px")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l8"), ("attr", cod([("align", "left")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([]))));
  outpvar.addtext(inp["dishinfo"]["title"]);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l4")]))));
  outpvar.cur.addfcdata("icon1");
  outpvar.addchilds(newtag_icon1(cod([("img", "photo/inr1.png")]), ginp, outpvar.cur.fcalldata["icon1"].root.content).root.content);
  outpvar.open(htmlnode("span", extentattrs(cod([("style", cod([("font-size", "25px"), ("font-weight", "600")]))]))));
  outpvar.addtext(inp["dishinfo"]["price"]);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row valign-wrapper"), ("attr", cod([("align", "left")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l2")]))));
  outpvar.cur.addfcdata("circleimg");
  outpvar.addchilds(newtag_circleimg(cod([("src", inp["dishinfo"]["profilepic"])]), ginp, outpvar.cur.fcalldata["circleimg"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l10")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("font-weight", "500")]))]))));
  outpvar.cur.addfcdata("profilea1");
  outpvar.addchilds(newtag_profilea1(cod([("text", myadd("Chef ", inp["dishinfo"]["name"])), ("uid", inp["dishinfo"]["cid"])]), ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([]))));
  outpvar.cur.addfcdata("starrating");
  outpvar.addchilds(newtag_starrating(cod([("val", 3)]), ginp, outpvar.cur.fcalldata["starrating"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  if (int((inp["islogin"] == "a"))): 
    outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l4 ")]))));
    outpvar.open(htmlnode("button", extentattrs(cod([("class", "btn waves-effect waves-light btn"), ("datas", cod([("datetime", inp["dishinfo"]["datetime"]), ("lord", inp["dishinfo"]["lord"]), ("dishid", inp["dishinfo"]["id"])])), ("data", cod([("onclick", "sreq"), ("action", "deletedisp"), ("restext", "Deleted !")]))]))));
    outpvar.addtext("Delete");
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l4 offset-l3")]))));
    outpvar.open(htmlnode("button", extentattrs(cod([("class", "btn waves-effect waves-light btn")]))));
    outpvar.addtext("Edit");
    outpvar.close();
    outpvar.close();
  elif (int((inp["loginid"] == inp["dishinfo"]["cid"]))): 
    pass
  elif (1): 
    outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l4 ")]))));
    outpvar.open(htmlnode("button", extentattrs(cod([("class", "btn waves-effect waves-light btn"), ("data", cod([("onclick", "addfav")])), ("attr", cod([("id", "mohit")]))]))));
    outpvar.addtext("Favourite");
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l4 offset-l3")]))));
    outpvar.open(htmlnode("button", extentattrs(cod([("class", "btn waves-effect waves-light btn"), ("data", cod([("onclick", "sreq"), ("action", "addincart"), ("restext", "Added!")])), ("datas", cod([("datetime", inp["dishinfo"]["datetime"]), ("lord", inp["dishinfo"]["lord"]), ("dishid", inp["dishinfo"]["id"])]))]))));
    outpvar.addtext("Add + ");
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_l_otp_button(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("button", extentattrs(cod([("class", "btn waves-effect waves-light"), ("attr", cod([("type", "button")])), ("data", cod([("onclick", "sreq"), ("action", "sendotp"), ("fobj", "$(obj).parent().parent()[0]"), ("restext", "Re-send")]))]))));
  outpvar.addtext("Send OTP");
  outpvar.close();
  return outpvar;
  
def newtag_loginmodal(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("attr", cod([("id", "loginmodal")])), ("class", "modal")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "modal-content container-fluid")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("ul", extentattrs(cod([("class", "tabs")]))));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("liclass", "tab col l6"), ("tablink", ["#logintab", "#signuptab"]), ("tabname", ["Login", "Signup"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("attr", cod([("id", "logintab")]))]))));
  outpvar.open(htmlnode("form", extentattrs(cod([("data", cod([("onsubmit", "sreq"), ("bobj", ""), ("action", "login"), ("res", "ms.reload();"), ("errorh", "error_login")]))]))));
  outpvar.cur.addfcdata("errorbox");
  outpvar.addchilds(newtag_errorbox(cod([]), ginp, outpvar.cur.fcalldata["errorbox"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.cur.addfcdata("input3");
  outpvar.addchilds(newtag_input3(cod([("label", "Phone"), ("icon", "phone"), ("aclass", "col s12 l7 m6"), ("name", "loginphone"), ("dc", "phone")]), ginp, outpvar.cur.fcalldata["input3"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l4 m6")]))));
  outpvar.cur.addfcdata("l_otp_button");
  outpvar.addchilds(newtag_l_otp_button(cod([]), ginp, outpvar.cur.fcalldata["l_otp_button"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.cur.addfcdata("input3");
  outpvar.addchilds(newtag_input3(cod([("label", "Password or OTP"), ("icon", "vpn_key"), ("aclass", "col s12 l12 m12"), ("name", "loginpass"), ("type", "password"), ("dc", "password1")]), ginp, outpvar.cur.fcalldata["input3"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col")]))));
  outpvar.open(htmlnode("button", extentattrs(cod([("class", "btn waves-effect waves-light"), ("attr", cod([("type", "submit")]))]))));
  outpvar.addtext("Login");
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("attr", cod([("id", "signuptab")]))]))));
  outpvar.open(htmlnode("form", extentattrs(cod([("data", cod([("onsubmit", "sreq"), ("bobj", ""), ("action", "signup"), ("res", "ms.reload();"), ("errorh", "error_login")]))]))));
  outpvar.cur.addfcdata("errorbox");
  outpvar.addchilds(newtag_errorbox(cod([]), ginp, outpvar.cur.fcalldata["errorbox"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.cur.addfcdata("input3");
  outpvar.addchilds(newtag_input3(cod([("label", "Phone number"), ("icon", "phone"), ("aclass", "col s12 l7 m6"), ("name", "signupphone"), ("dc", "phone")]), ginp, outpvar.cur.fcalldata["input3"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l4 m6")]))));
  outpvar.cur.addfcdata("l_otp_button");
  outpvar.addchilds(newtag_l_otp_button(cod([]), ginp, outpvar.cur.fcalldata["l_otp_button"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.cur.addfcdata("input3");
  outpvar.addchilds(newtag_input3(cod([("label", "Choose Password"), ("icon", "vpn_key"), ("aclass", "col s12 l6 m6"), ("name", "signuppass"), ("type", "password"), ("dc", "password1")]), ginp, outpvar.cur.fcalldata["input3"].root.content).root.content);
  outpvar.cur.addfcdata("input3");
  outpvar.addchilds(newtag_input3(cod([("label", "OTP"), ("icon", "vpn_key"), ("aclass", "col s12 l6 m6"), ("name", "signupotp"), ("type", "password"), ("dc", "otp")]), ginp, outpvar.cur.fcalldata["input3"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.cur.addfcdata("input3");
  outpvar.addchilds(newtag_input3(cod([("label", "Name"), ("icon", "account_circle"), ("aclass", "col s12 l12 m12"), ("name", "signupname")]), ginp, outpvar.cur.fcalldata["input3"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col")]))));
  outpvar.open(htmlnode("button", extentattrs(cod([("class", "btn waves-effect waves-light"), ("attr", cod([("type", "submit")]))]))));
  outpvar.addtext("Signup");
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_table1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("rows", []), ("thead", [])])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("table", extentattrs(cod([("class", inp["class"])]))));
  outpvar.open(htmlnode("thead", extentattrs(cod([]))));
  for i in forlist(inp["thead"], False ) :
    outpvar.open(htmlnode("th", extentattrs(cod([]))));
    outpvar.addtext(i);
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("tbody", extentattrs(cod([]))));
  for ii in forlist(inp["rows"], True ) :
    i = inp["rows"][ii];
    outpvar.open(htmlnode("tr", extentattrs(cod([]))));
    for jj in forlist(i, True ) :
      j = i[jj];
      outpvar.open(htmlnode("td", extentattrs(cod([]))));
      outpvar.addtext(j);
      outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_profilea1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("uid", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("text", inp["text"]), ("href", myadd(myadd(inp["BASE"], "profile?uid="), inp["uid"]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  return outpvar;
  
def newtag_account_admin(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("attr", cod([("align", "center")]))]))));
  outpvar.cur.addfcdata("height");
  outpvar.addchilds(newtag_height(cod([("val", 20)]), ginp, outpvar.cur.fcalldata["height"].root.content).root.content);
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv(cod([("text", "Hey Admin,\n you are welcome"), ("font", "20px")]), ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.cur.addfcdata("height");
  outpvar.addchilds(newtag_height(cod([("val", 50)]), ginp, outpvar.cur.fcalldata["height"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("table", extentattrs(cod([("class", "bordered striped centered highlight")]))));
  outpvar.open(htmlnode("thead", extentattrs(cod([]))));
  for i in forlist(["UserID", "Name", "Email", "Phone", "User Type"], False ) :
    outpvar.open(htmlnode("th", extentattrs(cod([]))));
    outpvar.addtext(i);
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("tbody", extentattrs(cod([]))));
  for ii in forlist(inp["users"], True ) :
    i = inp["users"][ii];
    outpvar.open(htmlnode("tr", extentattrs(cod([]))));
    for jj in forlist(["id", "name", "email", "phone", "typetext"], True ) :
      jjj = ["id", "name", "email", "phone", "typetext"][jj];
      inp["j"] = i[jjj];
      outpvar.open(htmlnode("td", extentattrs(cod([]))));
      if (int((int((jjj == "name")) and int((i["type"] == "c"))))): 
        outpvar.cur.addfcdata("profilea1");
        outpvar.addchilds(newtag_profilea1(cod([("text", inp["j"]), ("uid", i["id"])]), ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
      elif (1): 
        outpvar.addtext(inp["j"]);
      outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.cur.addfcdata("button1");
    outpvar.addchilds(newtag_button1(cod([("name", ("UnBlock" if (i["conf"]) else "Block")), ("datas", cod([("uid", i["id"]), ("isblock", int((i["conf"] != None)))])), ("data", cod([("onclick", "sreq"), ("action", "blockunblock"), ("restext", "Done!")]))]), ginp, outpvar.cur.fcalldata["button1"].root.content).root.content);
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_profile_chef_top2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row valign-wrapper")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l3"), ("attr", cod([("align", "center")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([]))));
  outpvar.cur.addfcdata("circleimg");
  outpvar.addchilds(newtag_circleimg(cod([("src", inp["uinfo"]["profilepic"])]), ginp, outpvar.cur.fcalldata["circleimg"].root.content).root.content);
  outpvar.close();
  if (inp["canedit"]): 
    outpvar.open(htmlnode("form", extentattrs(cod([("attr", cod([("enctype", "multipart/form-data"), ("method", "post")]))]))));
    outpvar.cur.addfcdata("a1");
    outpvar.addchilds(newtag_a1(cod([("text", "Upload Profile Pic"), ("attr", cod([("onclick", "uploadfile(this, \"profilepic\");")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
    outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([]))));
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv(cod([("text", myadd("Chef ", inp["uinfo"]["name"])), ("font", "25px"), ("fontw", "500")]), ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l6")]))));
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv(cod([("text", 38456), ("fontw", 600)]), ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv(cod([("text", "Plates Delivered")]), ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l6")]))));
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv(cod([("text", 56), ("fontw", 600)]), ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv(cod([("text", "People reviewed")]), ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_profile_chef(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "container-fluid")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l10 offset-l1 s10 m10 offset-s1 offset-m1")]))));
  outpvar.cur.addfcdata("profile_chef_top2");
  outpvar.addchilds(newtag_profile_chef_top2(cod([]), ginp, outpvar.cur.fcalldata["profile_chef_top2"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "msdivider")]))));
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "container-fluid")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_select1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tlist", []), ("class", "browser-default"), ("aclass", ""), ("selected", None), ("name", None), ("vlist", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("select", extentattrs(cod([("class", myadd(myadd(inp["class"], " "), inp["aclass"])), ("attr", inp["attr"])]))));
  if (int((inp["toptext"] != None))): 
    outpvar.open(htmlnode("option", extentattrs(cod([("attr", cod([("value", "")]))]))));
    outpvar.addtext(inp["toptext"]);
    outpvar.close();
  for ii in forlist(inp["tlist"], True ) :
    i = inp["tlist"][ii];
    inp["attrs"] = cod([]);
    if (int((inp["vlist"] != None))): 
      inp["attrs"]["value"] = inp["vlist"][ii];
    elif (1): 
      inp["attrs"]["value"] = myadd(ii, 1);
    if (int((inp["selected"] == ii))): 
      inp["attrs"]["selected"] = "";
    outpvar.open(htmlnode("option", extentattrs(cod([("attr", inp["attrs"])]))));
    outpvar.addtext(i);
    outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_select2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tlist", []), ("dclass", "col l3 s12 m6"), ("class", "browser-default"), ("selected", None), ("toptext", None), ("vlist", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", inp["dclass"])]))));
  outpvar.cur.addfcdata("select1");
  outpvar.addchilds(newtag_select1(cod([("class", inp["class"]), ("tlist", inp["tlist"]), ("vlist", inp["vlist"]), ("toptext", inp["toptext"]), ("selected", inp["selected"])]), ginp, outpvar.cur.fcalldata["select1"].root.content).root.content);
  outpvar.close();
  return outpvar;
  
def newtag_mselect(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tlist", []), ("vlist", None), ("selected", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  for ii in forlist(inp["tlist"], True ) :
    i = inp["tlist"][ii];
    inp["attrs"] = cod([]);
    if (int((inp["vlist"] != None))): 
      inp["attrs"]["value"] = inp["vlist"][ii];
    elif (1): 
      inp["attrs"]["value"] = myadd(ii, 1);
    if (int((inp["selected"] == ii))): 
      inp["attrs"]["selected"] = "";
    outpvar.cur.addfcdata("checkbox1");
    outpvar.addchilds(newtag_checkbox1(cod([("label", i), ("id", myadd(myadd(inp["id"], "_"), ii))]), ginp, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
  return outpvar;
  
def newtag_mselect1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tlist", []), ("vlist", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("id", inp["id"]), ("class", "dropdown-content p5"), ("tlist", [])]))));
  outpvar.cur.addfcdata("mselect");
  outpvar.addchilds(newtag_mselect(cod([("vlist", inp["vlist"]), ("tlist", inp["tlist"]), ("id", inp["id"])]), ginp, outpvar.cur.fcalldata["mselect"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("a", extentattrs(cod([("class", "dropdown-button"), ("data", cod([("activates", inp["id"])]))]))));
  outpvar.addtext(inp["label"]);
  outpvar.close();
  return outpvar;
  
def newtag_mselect2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("class", "col l3 s12 m6")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", inp["class"])]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "mselect complexinput"), ("data", cod([("complexinput", "ci_checkbox")])), ("attr", cod([("name", inp["id"])]))]))));
  outpvar.cur.addfcdata("mselect1");
  outpvar.addchilds(newtag_mselect1(cod([("id", inp["id"]), ("tlist", inp["tlist"]), ("label", inp["label"]), ("selectall", inp["selectall"])]), ginp, outpvar.cur.fcalldata["mselect1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_switch1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("on", "Yes"), ("off", "No")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "switch")]))));
  outpvar.open(htmlnode("label", extentattrs(cod([]))));
  outpvar.addtext(inp["off"]);
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("type", "checkbox"), ("name", inp["name"])]))]))));
  outpvar.open(htmlnode("span", extentattrs(cod([("class", "lever")]))));
  outpvar.close();
  outpvar.addtext(inp["on"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_switch2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("class", "col l3 s12 m6")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", inp["class"])]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "m5")]))));
  outpvar.addtext(inp["label"]);
  outpvar.cur.addfcdata("switch1");
  outpvar.addchilds(newtag_switch1(cod([("name", inp["name"])]), ginp, outpvar.cur.fcalldata["switch1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_orderl_admin(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("table", extentattrs(cod([("class", "bordered")]))));
  outpvar.open(htmlnode("thead", extentattrs(cod([]))));
  for i in forlist(["Odered At", "Delivery Date", "Chef", "User", "Dish", "Price", "Chef Address", "User Address", "Status"], False ) :
    outpvar.open(htmlnode("th", extentattrs(cod([]))));
    outpvar.addtext(i);
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("tbody", extentattrs(cod([]))));
  for ii in forlist(inp["orderl"], True ) :
    i = inp["orderl"][ii];
    outpvar.open(htmlnode("tr", extentattrs(cod([("class", "cartitems"), ("datas", cod([("datetime", i["datetime"]), ("cid", i["cid"]), ("lord", i["lord"]), ("dishid", i["dishid"])]))]))));
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.addtext(i["timetext"]);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.addtext(i["datetimetext"]);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.cur.addfcdata("profilea1");
    outpvar.addchilds(newtag_profilea1(cod([("text", i["cname"]), ("uid", i["cid"])]), ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.cur.addfcdata("profilea1");
    outpvar.addchilds(newtag_profilea1(cod([("text", i["uname"]), ("uid", i["uid"])]), ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.addtext(i["title"]);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.cur.addfcdata("icon1");
    outpvar.addchilds(newtag_icon1(cod([("img", "photo/inr2.png")]), ginp, outpvar.cur.fcalldata["icon1"].root.content).root.content);
    outpvar.open(htmlnode("span", extentattrs(cod([("class", "itemprice")]))));
    outpvar.addtext(myadd(myadd(myadd(myadd(i["price"], "*"), i["numplate"]), "="), (i["price"] * i["numplate"])));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.addtext(myadd(myadd(myadd(myadd(myadd("(", i["clat"]), ", "), i["clng"]), ")<br>"), i["caddress"]));
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.addtext(myadd(myadd(myadd(myadd(myadd("(", i["lat"]), ", "), i["lng"]), ")<br>"), i["uaddress"]));
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.addtext(i["status"]);
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_orderl_user(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("table", extentattrs(cod([("class", "bordered")]))));
  outpvar.open(htmlnode("thead", extentattrs(cod([]))));
  for i in forlist(["Odered At", "Delivery Date", "Chef", "Dish", "Price", "User Address", "Status"], False ) :
    outpvar.open(htmlnode("th", extentattrs(cod([]))));
    outpvar.addtext(i);
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("tbody", extentattrs(cod([]))));
  for ii in forlist(inp["orderl"], True ) :
    i = inp["orderl"][ii];
    outpvar.open(htmlnode("tr", extentattrs(cod([("class", "cartitems"), ("datas", cod([("datetime", i["datetime"]), ("cid", i["cid"]), ("lord", i["lord"]), ("dishid", i["dishid"])]))]))));
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.addtext(i["timetext"]);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.addtext(i["datetimetext"]);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.cur.addfcdata("profilea1");
    outpvar.addchilds(newtag_profilea1(cod([("text", i["cname"]), ("uid", i["cid"])]), ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.addtext(i["title"]);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.cur.addfcdata("icon1");
    outpvar.addchilds(newtag_icon1(cod([("img", "photo/inr2.png")]), ginp, outpvar.cur.fcalldata["icon1"].root.content).root.content);
    outpvar.open(htmlnode("span", extentattrs(cod([("class", "itemprice")]))));
    outpvar.addtext(myadd(myadd(myadd(myadd(i["price"], "*"), i["numplate"]), "="), (i["price"] * i["numplate"])));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.addtext(myadd(myadd(myadd(myadd(myadd("(", i["lat"]), ", "), i["lng"]), ")<br>"), i["uaddress"]));
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.addtext(i["status"]);
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_orderl_chef(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("table", extentattrs(cod([("class", "bordered")]))));
  outpvar.open(htmlnode("thead", extentattrs(cod([]))));
  for i in forlist(["Odered At", "Delivery Date", "User", "Dish", "Price", "User Address", "Status"], False ) :
    outpvar.open(htmlnode("th", extentattrs(cod([]))));
    outpvar.addtext(i);
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("tbody", extentattrs(cod([]))));
  for ii in forlist(inp["orderl"], True ) :
    i = inp["orderl"][ii];
    outpvar.open(htmlnode("tr", extentattrs(cod([("class", "cartitems"), ("datas", cod([("datetime", i["datetime"]), ("cid", i["cid"]), ("lord", i["lord"]), ("dishid", i["dishid"])]))]))));
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.addtext(i["timetext"]);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.addtext(i["datetimetext"]);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.cur.addfcdata("profilea1");
    outpvar.addchilds(newtag_profilea1(cod([("text", i["cname"]), ("uid", i["cid"])]), ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.cur.addfcdata("profilea1");
    outpvar.addchilds(newtag_profilea1(cod([("text", i["uname"]), ("uid", i["uid"])]), ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.addtext(i["title"]);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.cur.addfcdata("icon1");
    outpvar.addchilds(newtag_icon1(cod([("img", "photo/inr2.png")]), ginp, outpvar.cur.fcalldata["icon1"].root.content).root.content);
    outpvar.open(htmlnode("span", extentattrs(cod([("class", "itemprice")]))));
    outpvar.addtext(myadd(myadd(myadd(myadd(i["price"], "*"), i["numplate"]), "="), (i["price"] * i["numplate"])));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.addtext(myadd(myadd(myadd(myadd(myadd("(", i["clat"]), ", "), i["clng"]), ")<br>"), i["caddress"]));
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.addtext(myadd(myadd(myadd(myadd(myadd("(", i["lat"]), ", "), i["lng"]), ")<br>"), i["uaddress"]));
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs(cod([]))));
    outpvar.addtext(i["status"]);
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_orderl(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("utype", ginp["islogin"])])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  if (int((inp["utype"] == "u"))): 
    outpvar.cur.addfcdata("orderl_user");
    outpvar.addchilds(newtag_orderl_user(cod([("orderl", inp["orderl"])]), ginp, outpvar.cur.fcalldata["orderl_user"].root.content).root.content);
  if (int((inp["utype"] == "c"))): 
    outpvar.cur.addfcdata("orderl_chef");
    outpvar.addchilds(newtag_orderl_chef(cod([("orderl", inp["orderl"])]), ginp, outpvar.cur.fcalldata["orderl_chef"].root.content).root.content);
  if (int((inp["utype"] == "a"))): 
    outpvar.cur.addfcdata("orderl_admin");
    outpvar.addchilds(newtag_orderl_admin(cod([("orderl", inp["orderl"])]), ginp, outpvar.cur.fcalldata["orderl_admin"].root.content).root.content);
  return outpvar;
  
def newtag_errorbox(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row hiddenerror")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s12 l12")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "card-panel red white-text center errortext")]))));
  outpvar.addtext("");
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_menu_nofood(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l12 m12 s12")]))));
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv(cod([("text", "No chef is serving in this location. We are trying hard to serve you in this location, will let you know once this location is launched"), ("font", "20px")]), ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.close();
  return outpvar;
  
def newtag_kurry_footer(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "page-footer darken-4"), ("style", cod([("margin-bottom", "0px"), ("padding-bottom", "0px")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "container")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row"), ("style", cod([("margin-bottom", "-25px")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s2 m2 l3 offset-l2 offset-m2")]))));
  outpvar.open(htmlnode("h5", extentattrs(cod([]))));
  outpvar.addtext("Social Media");
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([]))));
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("text", "Facebook")]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("text", "Twitter")]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("text", "Instagram")]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s2 m2 l3")]))));
  outpvar.open(htmlnode("h5", extentattrs(cod([]))));
  outpvar.addtext("Help");
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([]))));
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("text", "About us"), ("attr", cod([("onclick", "$(\"#aboutus\").openModal();")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("text", "Contact us"), ("attr", cod([("onclick", "$(\"#contactusform\").openModal();")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s2 m2 l3")]))));
  outpvar.open(htmlnode("h5", extentattrs(cod([]))));
  outpvar.addtext("Legal");
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([]))));
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("text", "Company Policies, Terms and Conditions"), ("attr", cod([("onclick", "$(\"#policy\").openModal();")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l12 center ")]))));
  outpvar.addtext("&copy; Copyright 2015 KurryBox");
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_kurry_contactus_form(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s12 l12 m12")]))));
  outpvar.open(htmlnode("h3", extentattrs(cod([("class", "grey-text text-darken-4")]))));
  outpvar.addtext("Contact US");
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s12 l6 m6")]))));
  outpvar.open(htmlnode("h5", extentattrs(cod([("class", "grey-text text-darken-2")]))));
  outpvar.addtext("Mail");
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon(cod([("name", "mail"), ("aclass", "tiny")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "grey-text")]))));
  outpvar.addtext("kurrybox.contactus@gmail.com");
  outpvar.close();
  outpvar.open(htmlnode("h5", extentattrs(cod([("class", "grey-text text-darken-2")]))));
  outpvar.addtext("Call");
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon(cod([("name", "call"), ("aclass", "tiny")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "grey-text")]))));
  outpvar.addtext("+91 704 211 4473");
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_kurry_aboutus(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "card-content")]))));
  outpvar.open(htmlnode("h3", extentattrs(cod([("class", "card-title")]))));
  outpvar.addtext("About Us");
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([]))));
  outpvar.addtext(inp["aboutus_content"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_kurry_policy(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "card-content")]))));
  outpvar.open(htmlnode("h3", extentattrs(cod([("class", "card-title")]))));
  outpvar.addtext("Policy");
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([]))));
  outpvar.addtext(inp["policy_content"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  