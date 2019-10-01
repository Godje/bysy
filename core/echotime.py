from DB import DB;
from TIME import currentTime;
from TIME import timeDifference;

## Echo time function
def echotime(args, returnValue=False):
	db = DB().Load()

	if( db.Empty() ):
		print "Database is empty";
		return;
	last_item = db.LastItem();

	if(last_item['e'] != ""):
		print "No running jobs";
		return;
	else:
		time_now = currentTime();
		time_then = last_item['b'];
		time_difference = timeDifference(time_now, time_then);

	if(returnValue==True):
		return time_difference;
	else:
		print time_difference;
