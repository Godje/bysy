from DB import DB;
from datetime import datetime;

## Echo time function
def echotime(args):
	db = DB.load()

	if(len(db) == 0):
		print "Database is empty";
		return;
	last_item = db[-1];

	if(last_item['e'] != ""):
		print "No running jobs";
		return;
	else:
		time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S');
		time_then = last_item['b'];
		fmt = '%Y-%m-%d %H:%M:%S';
		tdelta = datetime.strptime(time_now, fmt) - datetime.strptime(time_then, fmt);
		output = str(tdelta);
		print output;
