## Stop function
from DB import DB;
from TIME import currentTime;

def stop(args):
	db = DB.load();
	if(len(db) == 0):
		print "Database is empty";
		return;
	last_item = db[-1];
	curr_time = currentTime();

	if( last_item['e'] == '' ):
		last_item['e'] = curr_time;
	else:
		print "Last job is completed. No jobs to stop";

	DB.save(db);
