from DB import DB;

class txtmodif:
	NORMAL = '\033[0m'
	BOLD = '\033[1m'
	WARNING = '\033[91m'

def get(args):
	db = DB().Load();
	return db.GetConfig(args[0]);

def listconfig(args):
	db = DB().Load();
	for obj in db.config:
		print "{0} = {1}".format(obj, db.config[obj]);
	return None;

def setvalue(args):
	print args;
	if(len(args) < 2):
		print "Not enough arguments!";
		return;
	db = DB().Load();
	db.SetConfig(args[0], args[1]);
	db.Save();
	return None;

def displayhelp(args):
	output="""
{0}CONFIG{1}
\t{0}get{1}\t- (Value) Returns the value (for internal/programmging use)
\t{0}list{1}\t- Lists all the configured values
\t{0}set{1}\t- (key, value) Set the value
\t{0}help{1}\t- Display this message

{0}VALUES{1}
\t{0}listmax{1}\t- (Number) Limits the amount of entries displayed on list command
	""";

	print output.format(txtmodif.BOLD, txtmodif.NORMAL);

def configure(args):
	db = DB().Load();
	if(len(args) < 1):
		displayhelp(args);
		return;
	def method(m):
		return {
				'get': get,
				'list': listconfig,
				'set': setvalue,
				'help': displayhelp
				}[m];
	
	return method(args[0])(args[1:]);

