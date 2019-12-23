from DB import DB;
from TIME import currentTime;
from TIME import timeDifference;
from configure import configure;

def loglist(args):
	argLength = len(args);

	db = DB().Load();
	if(len(db.database) == 0):
		print "Database is empty";
		return;
	reversed_list = db.database[::-1];

	if( argLength == 1 ):
		try:
			display_amount = int(args[0]);
		except ValueError:
			if(args[0] == "all" or args[0] == "csv"):
				display_amount = int(10000); # that's a dumb one, but still
			else:
				print "Undefined amount";
				return;
		reversed_list = reversed_list[ :display_amount ];
	else:
		maxentries = configure(["get", "listmax"]);
		if maxentries == None:
			maxentries = len(reversed_list);
		reversed_list = reversed_list[ :int( maxentries ) ]
	if(args[0] == "csv"):
		template = """{0},{1},{2},{3},{4}""";
	else:
		template = """{0} | {1} | {2} | {3} | {4}""";
	for entry in reversed_list:
		print template.format(
				entry['i'],
				entry['s'],
				entry['p'],
				entry['d'],
				timeDifference( entry['e'], entry['b'], stripseconds=True ))
