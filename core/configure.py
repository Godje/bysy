from DB import DB;


def get(arg):
	db = DB().Load();
	return db.GetConfig(arg[0]);

def listconfig(arg):
	db = DB().Load();
	for obj in db.config:
		print "{0} = {1}".format(obj, db.config[obj]);

def setvalue(args):
	if(len(args) < 2):
		print "Not enough arguments!";
		return;
	db = DB().Load();
	db.SetConfig(args[0], args[1]);
	db.Save();

def configure(*args):
	db = DB().Load();
	if(len(args) < 1):
		print "Not enough arguments;"
		return;
	def method(m):
		return {
				'get': get,
				'list': listconfig,
				'set': setvalue
				}[m];
	
	method(args[0])(args[1:]);
