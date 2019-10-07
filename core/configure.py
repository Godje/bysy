from DB import DB;


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

def configure(args):
	db = DB().Load();
	if(len(args[0]) < 1):
		print "Not enough arguments;"
		return;
	def method(m):
		return {
				'get': get,
				'list': listconfig,
				'set': setvalue
				}[m];
	
	return method(args[0])(args[1:]);
