from DB import DB;

class txtmodif:
	NORMAL = '\033[0m'
	BOLD = '\033[1m'
	WARNING = '\033[91m'

def create(args):
	db = DB().Load();
	if len(args) < 4:
		print "Not enough arguments";
		return;
	try:
		obj = {
				's': args[1],
				'p': args[2],
				'd': args[3]
				};
		db.alias[str(args[0])] = obj;
		db.Save();
		return;
	except:
		print "Error";
		return;

def getalias(args):
	db = DB().Load();
	try:
		result = db.alias[args[0]];
	except KeyError:
		result = None;
	return result;

def listalias(args):
	db = DB().Load();
	for alias in db.alias:
		a = db.alias[alias];
		print """\
{0}{2}{1} : {3} | {4} | {5}\
		""".format(txtmodif.BOLD, txtmodif.NORMAL, alias, a["s"], a["p"], a["d"]);
	return;

def printhelp(args):
	print """
{0}ALIAS{1}
\t{0}get{1}\t\t- (key) returns the value (for internal/programmging use)
\t{0}list{1}\t\t- lists all the configured values
\t{0}set|create{1}\t- ({0}Name{1}, {0}Sector{1}, {0}Project{1}, {0}Details{1}) set the value
\t{0}help{1}\t\t- display this message
	""".format(txtmodif.BOLD, txtmodif.NORMAL);
	return;

def alias(args):
	db = DB().Load();
	if(len(args) < 1):
		printhelp(args);
		return;
	def method(m):
		return {
				'create': create,
				'set': create,
				'get': getalias,
				'list': listalias,
				'help': printhelp
				}[m];
	try:
		return method(args[0])(args[1:]);
	except KeyError:
		print "\nWrong function.\n\tbysy alias help\n"
	return;
