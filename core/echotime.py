from DB import DB;
from TIME import currentTime;
from TIME import timeDifference;

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
		time_now = currentTime();
		time_then = last_item['b'];
		print timeDifference(time_now, time_then);
