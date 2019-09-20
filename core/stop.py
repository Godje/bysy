## Stop function
def stop():
	if(len(db) == 0):
		print "Database is empty";
		return;
	last_item = db[-1];
	current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S');

	if( last_item['e'] == '' ):
		last_item['e']= current_time;
	else:
		print "Last job is completed. No jobs to stop";

	save();
