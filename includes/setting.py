
execfile("includes/password.py");
if(_server == 'gcl'):
	HOST = 'http://poorvi.cse.iitd.ac.in/~cs1120233/kurry/';
	ROOT = '/home/btech/cs1120233/private_html/kurry/';
	db_data = {'host': 'poorvi.cse.iitd.ac.in', 'user': 'mohit', 'pass': 'mohitsaini', 'db': 'mohit'};
	_msladd = 'mslib/msl/'
elif(_server == 'csc'):
	HOST = 'http://privateweb.iitd.ac.in/~cs1120233/kurry/';
#	ROOT = '/home/btech/cs1120233/private_html/kurry/';
	ROOT = '/home/cse/btech/cs1120233/private_html/kurry/';
	db_data = {'host': 'poorvi.cse.iitd.ac.in', 'user': 'mohit', 'pass': 'mohitsaini', 'db': 'mohit'};
	_msladd = '~/.local/lib/python2.7/site-packages/msl/';
elif(_server == "aws"):
	HOST = 'http://54.149.49.212/kurry/';
	ROOT = '/var/www/html/kurry/';
	db_data = {'host': 'localhost', 'user': 'root', 'pass': 'mohit', 'db': 'kurry'};
elif(_server == "aws_kurry"):
	HOST = 'http://52.8.204.132/';
	HOST = 'http://kurrybox.in/';	
	ROOT = '/var/www/html/';
	db_data = {'host': 'localhost', 'user': 'root', 'pass': 'mohit', 'db': 'kurry'};
	_msladd = '/use/lib/python2.7/msl/';
elif(_server == "solnki"):
	HOST = 'http://localhost/kurry/';
	ROOT = '/var/www/html/kurry/';
	db_data = {'host': '10.208.20.8', 'user': 'mohit', 'pass': 'mohitsaini', 'db': 'mohit'};
	_mslad = '/usr/lib/python2.7/msl/';


CDN = HOST+'photo/'
BASE = HOST+'index.php/'
_mslib = ROOT+"mslib/";
_includes = [];
