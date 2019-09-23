## Stop function
import sys;
from DB import DB;
from datetime import datetime;

args = sys.argv;
argLength = len(args);

def stop(args):
	db = DB.load();
	if(len(db) == 0):
		print "Database is empty";
		return;
	last_item = db[-1];
	curr_time = current_time();

	if( last_item['e'] == '' ):
		last_item['e'] = curr_time;
	else:
		print "Last job is completed. No jobs to stop";

	DB.save(db);

def current_time():
	return datetime.now().strftime('%Y-%m-%d %H:%M:%S');
