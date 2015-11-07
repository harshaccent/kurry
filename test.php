<?php
echo microtime();
?>
<!DOCTYPE html>
<html>
  <head>
    <base href='http://poorvi.cse.iitd.ac.in/~cs1120233/kurry/' >
    <title>
      KurryBox
    </title>
    <link href='css/materialize.min.css'  type='text/css'  rel='stylesheet' >
    <link href='css/lib.css'  type='text/css'  rel='stylesheet' >
    <link href='css/materialize.min.css'  type='text/css'  rel='stylesheet' >
    <link href='css/custom-stylesheet.css'  type='text/css'  rel='stylesheet' >
    <link href='css/jquery.bxslider.css'  type='text/css'  rel='stylesheet' >
    <link href='css/lib.css'  type='text/css'  rel='stylesheet' >
    <link href='css/main.css'  type='text/css'  rel='stylesheet' >
    <link href='css/style.css'  type='text/css'  rel='stylesheet' >
  </head>
  <body style='background-image:url("photo/slide1.jpg");background-size:auto 100%;background-position:center' >
<div class='navbar-fixed ' >
  <nav role='container'  class='white' >
    <div class='nav-wrapper container' >
      <a href='http://poorvi.cse.iitd.ac.in/~cs1120233/kurry/index.php/'  id='logo-container'  class='brand-logo' >
        <img src='photo/mylogo1.png'  class='circle responsive-img'  style='vertical-align:middle' >
      </a>
      <ul class='right hide-on-med-and-down' >
        <li>
          <a href='http://poorvi.cse.iitd.ac.in/~cs1120233/kurry/'  class=' ' >
            Home
          </a>
        </li>
        <li>
          <a href=''  class=' ' >
            Our Story
          </a>
        </li>
        <li>
          <a href=''  class=' ' >
            Blog
          </a>
        </li>
        <li>
          <a href=''  class=' ' >
            Be a Chef
          </a>
        </li>
        <li>
          <a href=''  class=' ' >
            Contact Us
          </a>
        </li>
        <li>
          <a href='#loginmodal'  class='modal-trigger' >
            Login
          </a>
        </li>
      </ul>
      <ul id='nav-mobile'  class='side-nav' >
        <li>
          <a href='http://poorvi.cse.iitd.ac.in/~cs1120233/kurry/'  class=' ' >
            Home
          </a>
        </li>
        <li>
          <a href=''  class=' ' >
            Our Story
          </a>
        </li>
        <li>
          <a href=''  class=' ' >
            Blog
          </a>
        </li>
        <li>
          <a href=''  class=' ' >
            Be a Chef
          </a>
        </li>
        <li>
          <a href=''  class=' ' >
            Contact Us
          </a>
        </li>
      </ul>
      <a class='button-collapse'  data-activates='nav-mobile' >
        <i class='material-icons ' >
          menu
        </i>
      </a>
    </div>
  </nav>
</div>
  <div id='googlemap' >
  </div>
  <div>
    <div align='center' >
      <div class='pagecenter container' >
        <span style='color:white;text-shadow:3px 3px 3px #000, 2px 2px 2px blue;font-size:65px' >
          Super Hit Meal From Super Hit Chefs
        </span>
        <div style='height:40px' >
        </div>
        <form action='http://poorvi.cse.iitd.ac.in/~cs1120233/kurry/index.php/menu' >
          <div class='row'  style='background-color:' >
            <div class='col l1 m1' >
              &nbsp;
            </div>
            <div class='col m8 s12 l9'  style='padding:0px;margin:0px' >
              <input autofocus=''  placeholder='Enter Your Location'  id='locsearch'  class='bigsearch definput'  style='border-radius:0px' >
            </div>
            <div class='col m2 s12 l1 '  style='padding:0px;margin:0px' >
              <button type='submit'  class='bigsearchbutton waves-effect waves-light btn'  style='border-radius:0px' >
                Go
                <i class='material-icons right' >
                  send
                </i>
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
  <div id='loginmodal'  class='modal' >
    <div class='modal-content container-fluid' >
      <div class='row' >
        <ul class='tabs' >
          <li class='tab col l6' >
            <a href='#logintab'  class=' ' >
              Login
            </a>
          </li>
          <li class='tab col l6' >
            <a href='#signuptab'  class=' ' >
              Signup
            </a>
          </li>
        </ul>
      </div>
      <div id='logintab' >
        <form data-onsubmit='sreq'  data-action='login'  data-res='ms.reload();'  data-bobj='' >
          <div class='row' >
            <div class='input-field col s12 l7 m6' >
<i class='material-icons prefix' >
  phone
</i>
              <input type='text'  id='loginphone' >
              <label for='loginphone' >
                Phone number
              </label>
            </div>
            <div class='col l4 m6' >
              <button data-action='sendotp'  data-onclick='sreq'  data-restext='Re-send'  data-fobj='$(obj).parent().parent()[0]'  type='button'  class='btn waves-effect waves-light' >
                Send OTP
              </button>
            </div>
          </div>
          <div class='row' >
            <div class='input-field col s12 l12 m12' >
<i class='material-icons prefix' >
  vpn_key
</i>
              <input type='text'  id='loginpass' >
              <label for='loginpass' >
                Password or OTP
              </label>
            </div>
          </div>
          <div class='row' >
            <div class='col' >
              <button type='submit'  class='btn waves-effect waves-light' >
                Login
              </button>
            </div>
          </div>
        </form>
      </div>
      <div id='signuptab' >
        <form data-onsubmit='sreq'  data-action='signup'  data-res='ms.reload();'  data-bobj='' >
          <div class='row' >
            <div class='input-field col s12 l7 m6' >
<i class='material-icons prefix' >
  phone
</i>
              <input type='text'  id='signupphone' >
              <label for='signupphone' >
                Phone number
              </label>
            </div>
            <div class='col l4 m6' >
              <button data-action='sendotp'  data-onclick='sreq'  data-restext='Re-send'  data-fobj='$(obj).parent().parent()[0]'  type='button'  class='btn waves-effect waves-light' >
                Send OTP
              </button>
            </div>
          </div>
          <div class='row' >
            <div class='input-field col s12 l6 m6' >
<i class='material-icons prefix' >
  vpn_key
</i>
              <input type='password'  id='signuppass' >
              <label for='signuppass' >
                Choose Password
              </label>
            </div>
            <div class='input-field col s12 l6 m6' >
<i class='material-icons prefix' >
  vpn_key
</i>
              <input type='text'  id='signupotp' >
              <label for='signupotp' >
                OTP
              </label>
            </div>
          </div>
          <div class='row' >
            <div class='input-field col s12 l12 m12' >
<i class='material-icons prefix' >
  account_circle
</i>
              <input type='text'  id='signupname' >
              <label for='signupname' >
                Name
              </label>
            </div>
          </div>
          <div class='row' >
            <div class='col' >
              <button type='submit'  class='btn waves-effect waves-light' >
                Signup
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
    <script type='text/javascript' >
      var jsdata = {"_ec": {"-1": "Incorrect password or OTP", "-6": "Invalid Input", "-5": "Insufficient arguments", "-4": "Action handler not valid", "-3": "OTP is Incorrect", "-2": "Phone number already registered"}, "islogin": "", "HOST": "http://poorvi.cse.iitd.ac.in/~cs1120233/kurry/", "BASE": "http://poorvi.cse.iitd.ac.in/~cs1120233/kurry/index.php/", "curpage": "index", "_server": "gcl", "loginid": null};
    </script>
    <script type='text/javascript' >
      var ec  = jsdata['_ec'] ;
    </script>
    <script src='mslib/js/jquery-2.1.1.min.js'  type='text/javascript' >
    </script>
    <script src='mslib/js/materialize.min.js'  type='text/javascript' >
    </script>
    <script src='mslib/js/jquery.bxslider.min.js'  type='text/javascript' >
    </script>
    <script src='mslib/js/jquery.easing.1.3.js'  type='text/javascript' >
    </script>
    <script src='mslib/js/jquery.raty.js'  type='text/javascript' >
    </script>
    <script src='mslib/js/lib.js'  type='text/javascript' >
    </script>
    <script src='mslib/js/mohit.js'  type='text/javascript' >
    </script>
    <script src='mslib/js/mohitlib.js'  type='text/javascript' >
    </script>
    <script src='mslib/js/main.js'  type='text/javascript' >
    </script>
    <script src='js/main.js'  type='text/javascript' >
    </script>
    <script src='js/index.js'  type='text/javascript' >
    </script>
  </body>
</html>
<?php
echo microtime();
?>
