## Echo time function
def echotime():
	if(len(db) == 0):
		print "Database is empty";
		return;
	last_item = db[-1];

	if(last_item['e'] != ""):
		print "No running jobs";
		return;
	else:
		time_now = current_time();
		time_then = last_item['b'];
		fmt = '%Y-%m-%d %H:%M:%S';
		tdelta = datetime.strptime(time_now, fmt) - datetime.strptime(time_then, fmt);
		output = str(tdelta);
		print output;
