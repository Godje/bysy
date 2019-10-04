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

## Modules
from core.start import start;
from core.stop import stop;
from core.loglist import loglist;
from core.printhelp import printhelp;
from core.echotime import echotime;
from core.deleteentry import deleteentry;
from core.resume import resume;
from core.configure import configure;

## Checking for arguments
args = sys.argv;
argLength = len(args);

def main():
	def method(m):
		return {
				'start': start,
				'resume': resume,

				'pause': stop,
				'stop': stop,

				'list': loglist,
				'ls': loglist,
				'log': loglist,

				'help': printhelp,
				'time': echotime,
				'delete': deleteentry,
				'config': configure
				}[m];

	if( argLength > 1 ):
		method( args[1].lower() )(args[2:]);
	else:
		printhelp(0);

main();
