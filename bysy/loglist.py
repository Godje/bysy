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

	template = """{0} | {1} | {2} | {3} | {4}""";
	if( argLength == 1 ):
		template = """{0} | {1} | {2} | {3} | {4}""";

		try:
			display_amount = int(args[0]);
		except (ValueError, IndexError):
			if(args[0] == "all"):
				display_amount = int(10000); # that's a dumb one, but still
			elif(args[0] == "csv"):
				display_amount = int(10000);
				template = """{0},{1},{2},{3},{4}""";
			else:
				print "Undefined amount";
				return;
		reversed_list = reversed_list[ :display_amount ];
	else:
		maxentries = configure(["get", "listmax"]);
		if maxentries == None:
			maxentries = len(reversed_list);
		reversed_list = reversed_list[ :int( maxentries ) ]
	for entry in reversed_list:
		print template.format(
				entry['i'],
				entry['s'],
				entry['p'],
				entry['d'],
				timeDifference( entry['e'], entry['b'], stripseconds=True ))
