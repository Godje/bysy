import os.path;
import json;
import sys;

class txtmodif:
	NORMAL = '\033[0m'
	BOLD = '\033[1m'
	WARNING = '\033[91m'

cfgfilename = os.path.dirname(__file__)+"/config.json";

class Config:
	config = {};

	def Load(self):
		try:
			with open(cfgfilename) as cfgfile:
				self.config = json.loads(cfgfile.read());
			return self;
		except: 
			print "Error opening the config file. \nThis is a bug";
			sys.exit();
	
	def Save(self):
		with open(cfgfilename, 'w') as cfgfile:
			json.dump(self.config, cfgfile);

	def Get(self, key):
		value = None;
		try:
			value = self.config[key[0]];
			return value;
		except IndexError:
			raise ValueError("No key specified");
		except KeyError:
			raise ValueError("No value configured for this key");
		return None;

	def List(self):
		for entry in self.config:
			print "{0} = {1}".format(entry, self.config[entry])
		return;
	
	def Set(self, key, value):
		self.config[key] = value;
		self.Save();
		return;

def printhelp(args):
	output="""
{0}CONFIG{1}
\t{0}get{1}\t- (Value) Returns the value (for internal/programmging use)
\t{0}list{1}\t- Lists all the configured values
\t{0}set{1}\t- (key, value) Set the value
\t{0}help{1}\t- Display this message

{0}VALUES{1}
\t{0}listmax{1}\t\t- (Number) Limits the amount of entries displayed on list command
\t{0}db_location{1}\t- (Path) Location of the database JSON file, if you have a custom one
	""";

	print output.format(txtmodif.BOLD, txtmodif.NORMAL);

def setvalue(*args):
	config = Config()
	config.Load();
	try:
		config.Set( args[0][0], args[0][1] )
	except IndexError:
		print "No key or value specified";
		return;

def listconfig(*args):
	config = Config().Load();
	config.List();

def get(key):
	config = Config();
	config.Load();
	try:
		return config.Get(key)
	except:
		return None;

def configure(args):
	if(len(args) < 1):
		printhelp(args);
		return;
	def method(m):
		return {
				'get': get,
				'list': listconfig,
				'set': setvalue,
				'help': printhelp
				}[m];
	
	return method(args[0])(args[1:]);
