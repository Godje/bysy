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
# you execute the command, so the performance and memory consumption doesn't
# really matter here

import sys;
import json;
from datetime import time;
from datetime import datetime;
from textformat import txtmodif;

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
			'help': printhelp
		}[m];
	if( argLength > 1 ):
		method( args[1] )();
	else:
		printhelp();

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
	print json.dumps(db);

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
	for entry in db:
		print template.format(entry['i'], entry['s'], entry['p'], entry['d'], entry['b'], entry['e'])

def printhelp():
	help_string = """{0}\
	Available methods:{1}
		start stop list time"""

	print help_string.format(txtmodif.BOLD, txtmodif.NORMAL)

def save():
	with open(dbfilename, 'w') as dbfile:
		json.dump(db, dbfile)

main();

# Don't forget to read over JSON stuff
