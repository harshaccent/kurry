import json, datetime, pytz, time, re, copy, inspect, itertools, MySQLdb, sys, os
from time import mktime

execfile("includes/password.py");
if(_server == 'gcl'):
	HOST = 'http://poorvi.cse.iitd.ac.in/~cs1120233/kurry/';
	ROOT = '/home/btech/cs1120233/private_html/kurry/';
	db_data = {'host': 'poorvi.cse', 'user': 'mohit', 'pass': 'mohitsaini', 'db': 'mohit'};
elif(_server == "aws"):
	HOST = 'http://54.149.49.212/kurry/';
	ROOT = '/var/www/html/kurry/';
	db_data = {'host': 'localhost', 'user': 'root', 'pass': 'mohit', 'db': ''};

CDN = HOST+'photo/'
BASE = HOST+'index.php/'
_mslib = ROOT+"mslib/";
