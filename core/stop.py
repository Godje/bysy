## Stop function
from DB import DB;
from TIME import currentTime;

def stop(args):
	db = DB().Load();
	if( db.Empty() ):
		print "Database is empty";
		return;

	last_item = db.LastItem();
	curr_time = currentTime();

	if( last_item['e'] == '' ):
		last_item['e'] = curr_time;
	else:
		print "Last job is completed. No jobs to stop";

	DB.save(db.database);
