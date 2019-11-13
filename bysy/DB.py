import sys;
import json;
import os.path;
from operator import itemgetter;
from configure import configure;

def dbfilename():
	try:
		output = configure(["get", "db_location"]);
		if( output == None ):
			raise ValueError();
		else:
			return output;
	except:
		return os.path.dirname(__file__)+"/db.json";

class DB:
	database = [];
	alias = {};

	@staticmethod
	def load():
		db = [];
		try:
			with open( dbfilename() ) as dbfile:
				db = json.loads(dbfile.read());
		except ValueError: 
			print "Database doesn't exist.";
			print "To create a database execute the following shell command:";
			print "bysy.py init";
			sys.exit();
			return 0;
		return db;

	@staticmethod
	def save(*args):
		var1 = DB.load();

		db = args[0] if len(args) > 0 else [];
		alias = args[1] if len(args) > 1 else var1['alias'];

		var1['db'] = db;
		var1['alias'] = alias;
		with open(dbfilename(), 'w') as dbfile:
			json.dump(var1, dbfile);

	@staticmethod
	def find(key, value, db=None):
		if(db == None):
			db = DB.load().db;
		for entry in db:
			if entry[key] == int(value):
				return db.index(entry);
		return None;

	@staticmethod
	def lastIndex(db=None):
		if(db == None):
			db = DB.load();
		if(len(db) == 0):
			return 0;
		idlist = [];
		for entry in db:
			idlist.append((
				entry['i'],
				db.index(entry)
				));
		lastEntry = max(idlist, key=itemgetter(1));
		return lastEntry[1];

	@staticmethod
	def lastItem(db=None):
		if(db == None):
			db = DB.load();
		if(len(db) == 0):
			return {'i': 0};
		return db[ DB.lastIndex(db) ];

	@staticmethod
	def empty():
		db = DB.load();
		return len(db) < 1;
	
	def Load(self):
		dbloaded = DB.load();
		self.database = dbloaded["db"];
		self.alias = dbloaded["alias"];
		self.lastId = self.Find('i', self.LastIndex());
		return self;

	def Save(self):
		DB.save(self.database, self.alias);
		return self;

	def Empty(self):
		return len(self.database) == 0;

	def LastIndex(self):
		return DB.lastIndex(db=self.database);

	def LastItem(self):
		return self.lastItem(db=self.database);

	def Find(self, key, value):
		return DB.find(key, value, db=self.database)

	def SetAlias(self, key, value):
		self.alias[key] = value;
		return True;

	def GetAlias(self, key):
		try:
			return self.alias[key];
		except KeyError:
			return None;

	def SetConfig(self, key, value):
		self.config[key] = value;
		return True;

	def GetConfig(self, key):
		try:
			return self.config[key];
		except KeyError:
			return None;
