import sys;
from DB import DB;

args = sys.argv;
argLength = len(args);

## Start function
def start():
	db = DB.load();
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

	if( argLength < 5 ):
		print "Not enough arguments";
		return;

	current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S');
	entry = {
			'i': last_id() + 1,
			's': args[2],
			'p': args[3],
			'd': args[4],
			'c': '',
			'b': current_time,
			'e': "",
			};
	if( argLength == 6 ):
		entry['c'] = args[5]

	db.append(entry);

	return_message = """{5}\
			Starting a log:{6}
		id: {5}{0}{6}
		sector: {5}{1}{6}
		project: {5}{2}{6}
		description: {5}{3}{6}
				{7}
		start_time: {5}{4}"""
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

	DB.save(db);
