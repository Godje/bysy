from DB import DB;
from TIME import currentTime;
from TIME import timeDifference;

def loglist(args):
	argLength = len(args);

	db = DB.load();

	reversed_list = db[::-1];
	if( argLength == 3 and int(args[2]) > 0):
		reversed_list = reversed_list[ :int(args[2]) ];
	print "Here's the list:";
	template = """{0} | {1} | {2} | {3} | {4}""";
	for entry in reversed_list:
		print template.format(
				entry['i'],
				entry['s'],
				entry['p'],
				entry['d'],
				timeDifference( entry['e'], entry['b'], stripseconds=True ))
