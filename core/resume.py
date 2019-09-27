from DB import DB;
from start import start;

## Start function
def resume(args):
	db = DB().Load();
	if(len(args) > 0):
		index = db.Find('i', args[0]);
	else:
		index = db.LastIndex();
	entry = db.database[index];
	if(entry != None):
		startArgs = [entry['s'], entry['p'], entry['d']]
		start(startArgs);
