#!/usr/bin/python

# Author: Daniel Mayovskiy
#
# Literally my first Python program, so don't be surprised for noob memory
# management
#
# So don't be surprised that I have a bunch of Guard conditional statements
# I use every hack that will make the code look nice and readable, instead
# of code being performant. 
#
# It's a very short script that will run each time
# you execute the command, so the performance and memory consumption don't
# really matter here

import sys;
import json;
from datetime import time;
from datetime import datetime;

dbfilename = "db.json";
with open(dbfilename) as dbfile:
	db = json.loads(dbfile.read());

args = sys.argv;
argLength = len(args);

def main():
	def method(m):
		return {
			'start': start,
			'stop': stop,
			'list': loglist,
			'help': printhelp,
			'time': echotime,
			'delete': deletelog
		}[m];

	if( argLength > 1 ):
		method( args[1] )();
	else:
		printhelp();

def current_time():
	return datetime.now().strftime('%Y-%m-%d %H:%M:%S');

def start():
	def last_id():
		max_id = 0;
		if(len(db) == 0):
			return 0;
		for entry in db:
			if (entry['i'] > max_id):
				max_id = entry['i']
		return max_id;

	if( len(db) != 0 and db[-1]['e'] == "" ):
		print "There is another Log running at the moment";
		return;

	if( argLength != 5 ):
		print "Not enough arguments";
		return;
	
	current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S');
	entry = {
			'i': last_id() + 1,
			's': args[2],
			'p': args[3],
			'd': args[4],
			'b': current_time,
			'e': "",
			}

	db.append(entry);

	return_message = """{5}\
	Starting a log:{6}
		id: {5}{0}{6}
		sector: {5}{1}{6}
		project: {5}{2}{6}
		description: {5}{3}{6}
		start_time: {5}{4}"""
	print return_message.format( 
			entry['i'],		# {0}
			entry['s'],		# {1}
			entry['p'],		# {2}
			entry['d'],		# {3}
			entry['b'],		# {4}
			txtmodif.BOLD,	# {5} //first text modifier
			txtmodif.NORMAL	# {6} //second text modifier
			)

	save();

def stop():
	if(len(db) == 0):
		print "Datase is empty";
		return;
	last_item = db[-1];
	current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S');

	if( last_item['e'] == '' ):
		last_item['e']= current_time;
	else:
		print "Last job is completed. No jobs to stop";

	save();

def loglist():
	print "Here's the list:";
	template = """{0} | {1} | {2} | {3} | {4} | {5}""";
	for entry in reversed(db):
		print template.format(entry['i'], entry['s'], entry['p'], entry['d'], entry['b'], entry['e'])

def printhelp():
	help_string = """{0}\

Available methods:{1}

	{0}start{1}   - (Sector, Project, Description) starts a new Log
	{0}stop{1}    - stops the last log
	{0}list{1}    - lists logs
	{0}time{1}    - tells how much time has passed since the last log
	{0}delete{1}  - delets a selected log
	{0}help{1}    - displays this help message
        """
	print help_string.format(txtmodif.BOLD, txtmodif.NORMAL)

def echotime():
	time_now = current_time();
	last_item = db[-1];

	if(len(db) == 0):
		print "Database is empty";
		return;

	if(last_item['e'] != ""):
		print "No running jobs";
		return;
	else:
		time_then = last_item['b'];
		fmt = '%Y-%m-%d %H:%M:%S';
		tdelta = datetime.strptime(time_now, fmt) - datetime.strptime(time_then, fmt);
		output = str(tdelta);
		print output;

def deletelog():
	if(len(db) == 0):
		print "Database is empty";
		return;

	if( argLength < 3 ):
		print "Not enough arguments provided";
		return;
	else:
		item_index = find(db, 'i', args[2]);
		if(item_index != None):
			del db[item_index];
			save();
		else:
			print "No item with such id";
			return;

def find(lst, key, value):
	for entry in lst:
		if entry[key] == int(value):
			return lst.index(entry);
	return None;


def save():
	with open(dbfilename, 'w') as dbfile:
		json.dump(db, dbfile)

class txtmodif:
    NORMAL = '\033[0m'
    BOLD = '\033[1m'
    WARNING = '\033[91m'

main();
