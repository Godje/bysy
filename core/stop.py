## Stop function
from DB import DB;
from TIME import currentTime;

from echotime import echotime;

def stop(args):
	db = DB().Load();
	if( db.Empty() ):
		print "Database is empty";
		return;

	last_item = db.LastItem();
	curr_time = currentTime();

	if( last_item['e'] == '' ):
		last_item['e'] = curr_time;
		print "Stopped. Time elapsed: {}".format( echotime(args, returnValue=True) );
	else:
		print "Last job is completed. No jobs to stop";

	DB.save(db.database);
