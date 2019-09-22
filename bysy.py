#!/usr/bin/python

# Author: Daniel Mayovskiy
#
# Literally my first Python program, so don't be surprised for noob memory
# management
#
# Don't be surprised that I have a bunch of Guard conditional statements
# I use every hack that will make the code look nice and readable, instead
# of code being performant. 
#
# It's a very short script that will run each time
# you execute the command, so the performance and memory consumption don't
# really matter here

import sys;

from datetime import datetime;

## Modules
from core.start import start;
from core.stop import stop;
from core.loglist import loglist;
from core.printhelp import printhelp;
from core.echotime import echotime;
from core.deleteentry import deleteentry;

## Checking for arguments
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
				'delete': deleteentry
				}[m];

	if( argLength > 1 ):
		method( args[1] )();
	else:
		printhelp();

## Helper functions
def current_time():
	return datetime.now().strftime('%Y-%m-%d %H:%M:%S');

def find(lst, key, value):
	for entry in lst:
		if entry[key] == int(value):
			return lst.index(entry);
	return None;

main();
