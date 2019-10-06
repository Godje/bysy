from DB import DB;
from shutil import copyfile;

def initialize(args):
	print "This command will overwrite any existing database. \nPlease, back up your previous database.";
	print "Are you sure you want to proceed? [Y/n]";

	s = str(raw_input());
	correct = ['', 'y', 'yes'];

	if ( s not in correct ):
		print "Initialization cancelled";
		return;
	else:
		print "Creating a database";
		copyfile('template.json', 'db.json');
	return 1;
