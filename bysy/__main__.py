#!/usr/bin/python

import sys;

## Checking for arguments
args = sys.argv;
argLength = len(args);

class txtmodif:
	NORMAL = '\033[0m'
	BOLD = '\033[1m'
	WARNING = '\033[91m'

def edit(args):
	import os;
	from DB import dbfilename;
	if( len(os.environ.get("EDITOR")) == 0 or os.getenv("EDITOR", True) == True):
		print "$EDITOR environment variable is not defined";
		return;
	else:
		os.system("$EDITOR " + dbfilename());
	return;

def printhelp(args):
	help_string = """{0}\

Available methods:{1}
\t{0}start{1}\t\t- ({0}Sector{1}, {0}Project{1}, {0}Description{1}) starts a new Log
\t{0}stop|pause{1}\t- stops the last log
\t{0}list|ls|log{1}\t- lists logs
\t{0}time{1}\t\t- tells how much time has passed since the last log
\t{0}delete{1}\t\t- deletes a selected log
\t{0}resume{1}\t\t- resumes a the last task. Or the task at <id> you specify
\t{0}config{1}\t\t- manage configuration
\t{0}help{1}\t\t- displays this help message
\t{0}edit{1}\t\t- opens the database file in $EDITOR
\t{0}config{1}\t\t- (further command) displays this help message
\t{0}alias{1}\t\t- (further command) displays this help message

{0}CONFIG{1}
\t{0}get{1}\t\t- (key) returns the value (for internal/programming use)
\t{0}list{1}\t\t- lists all the configured values
\t{0}set{1}\t\t- ({0}Key{1}, {0}Value{1}) set the value
\t{0}help{1}\t\t- display this message

{0}ALIAS{1}
\t{0}get{1}\t\t- (key) returns the value (for internal/programmging use)
\t{0}list{1}\t\t- lists all the configured values
\t{0}set|create{1}\t- ({0}Name{1}, {0}Sector{1}, {0}Project{1}, {0}Details{1}) set the value
\t{0}help{1}\t\t- display this message
		""";
	print help_string.format(txtmodif.BOLD, txtmodif.NORMAL);

def main():
	if( argLength > 1 ):
		try:
			from start import start;
			from stop import stop;
			from loglist import loglist;
			from echotime import echotime;
			from deleteentry import deleteentry;
			from resume import resume;
			from configure import configure;
			from initialize import initialize;
			from alias import alias;

			def method(m):
				return {
						'init':initialize,
						'edit':edit,

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

			method( args[1].lower() )(args[2:]);
		except KeyError:
			print args[1];
			print "\nWrong function. Check out:\n\tbysy.py help\n";
	else:
		printhelp(0);

