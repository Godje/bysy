from DB import DB;
from TIME import currentTime;
from TIME import timeDifference;

def loglist(args):
	argLength = len(args);

	db = DB.load();
	if(len(db) == 0):
		print "Database is empty";
		return;
	reversed_list = db[::-1];
	if( argLength == 1 ):
		reversed_list = reversed_list[ :int(args[0]) ];
	template = """{0} | {1} | {2} | {3} | {4}""";
	for entry in reversed_list:
		print template.format(
				entry['i'],
				entry['s'],
				entry['p'],
				entry['d'],
				timeDifference( entry['e'], entry['b'], stripseconds=True ))
