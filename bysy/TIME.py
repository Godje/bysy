from datetime import datetime;
from datetime import timedelta;

def currentTime():
	return datetime.now().strftime('%Y-%m-%d %H:%M:%S');

def timeDifference(time1, time2, stripseconds=False):
	fmt='%Y-%m-%d %H:%M:%S';
	if( not time1 or not time2 ):
		return "Undefined/ongoing";
	tdelta = datetime.strptime(time1, fmt) - datetime.strptime(time2, fmt);
	output = str(tdelta);
	if(stripseconds):
		output = ':'.join((output).split(':')[:2]);
	return output;
