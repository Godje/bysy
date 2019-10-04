import sys;
import json;
from operator import itemgetter;

dbfilename = "db.json";

class DB:
	database = [];
	config = {};

	@staticmethod
	def load():
		db = [];
		try:
			with open(dbfilename) as dbfile:
				db = json.loads(dbfile.read());
		except: 
			print "Database doesn't exist.";
			print "To create a database execute the following shell command:";
			print "echo \"[]\" > db.json";
			sys.exit();
			return 0;
		return db;

	@staticmethod
	def save(*args):
		var1 = DB.load();

		db = args[0] if len(args) > 0 else [];
		config = args[1] if len(args) > 1 else var1['config'];

		var1['db'] = db;
		var1['config'] = config;
		with open(dbfilename, 'w') as dbfile:
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
		self.config = dbloaded["config"];
		self.lastId = self.Find('i', self.LastIndex());
		return self;

	def Save(self):
		print self.database, self.config;
		DB.save(self.database, self.config);
		return self;

	def Empty(self):
		return len(self.database) == 0;

	def LastIndex(self):
		return DB.lastIndex(db=self.database);

	def LastItem(self):
		return self.lastItem(db=self.database);

	def Find(self, key, value):
		return DB.find(key, value, db=self.database)

	def SetConfig(self, key, value):
		self.config[key] = value;
		return True;

	def GetConfig(self, key):
		try:
			return self.config[key];
		except KeyError:
			print "Error";
