from DB import DB;
from TIME import currentTime;
from alias import alias;

## Start function
def start(args):
	argLength = len(args);

	if(argLength == 2):
		print "Not enough arguments";

	db = DB().Load();

	if( not db.Empty() and db.LastItem()['e'] == "" ):
		print "There is another entry running at the moment";
		return;

	current_time = currentTime();
	entry = {
			'i': db.LastItem()['i'] + 1,
			'c': '',
			'b': current_time,
			'e': "",
			};

	if( argLength == 1 ):
		try:
			e = alias(["get", args[0]]);
			entry["s"] = e["s"];
			entry["p"] = e["p"];
			entry["d"] = e["d"];
		except TypeError:
			print "No alias found with name {}".format(args[0]);
			return;
	elif( argLength >= 3):
		entry["s"] = args[0];
		entry["p"] = args[1];
		entry["d"] = args[2];
		entry["c"] = args[3] if argLength == 4 else ""; 

	db.database.append(entry);

	return_message = """{5}
Starting a log:{6}
	id: {5}{0}{6}
	sector: {5}{1}{6}
	project: {5}{2}{6}
	description: {5}{3}{6}
	{7}
	start_time: {5}{4}
	"""
	print return_message.format( 
			entry['i'],		# {0}
			entry['s'],		# {1}
			entry['p'],		# {2}
			entry['d'],		# {3}
			entry['b'],		# {4}
			txtmodif.BOLD,			# {5} //first text modifier
			txtmodif.NORMAL,		# {6} //second text modifier
			"comments: " + str(entry['c'])
			)

	db.Save();

class txtmodif:
	NORMAL = '\033[0m'
	BOLD = '\033[1m'
	WARNING = '\033[91m'
