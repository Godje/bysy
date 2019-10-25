#!/usr/bin/python

# Author: Daniel Mayovskiy
#
# Literally my first Python program, so don't be surprised for noob memory
# management
#
# Don't be surprised that I have a bunch of Guard conditional statements
# I use every hack that will make the code look nice and readable, 
# prioritized over minute performance optimizations.
#
# It's a very short script that will run each time
# you execute the command, so the performance and memory consumption don't
# really matter here

import sys;

## Modules
from start import start;
from stop import stop;
from loglist import loglist;
from printhelp import printhelp;
from echotime import echotime;
from deleteentry import deleteentry;
from resume import resume;
from configure import configure;
from initialize import initialize;
from alias import alias;

## Checking for arguments
args = sys.argv;
argLength = len(args);

def main():
	def method(m):
		return {
				'init':initialize,

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
				'config': configure,
				'alias': alias
				}[m];

	if( argLength > 1 ):
		try:
			method( args[1].lower() )(args[2:]);
		except KeyError:
			print args[1]
			print "\nWrong function. Check out:\n\tbysy.py help\n"
	else:
		printhelp(0);
