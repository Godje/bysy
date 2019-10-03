import sys;
import json;
from operator import itemgetter;

dbfilename = "db.json";

class DB:
	database = [];

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
	def save(db):
		with open(dbfilename, 'w') as dbfile:
			json.dump(db, dbfile);

	@staticmethod
	def find(key, value, db=None):
		if(db == None):
			db = DB.load();
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
		self.database = DB.load();
		self.lastId = self.Find('i', self.LastIndex());
		return self;

	def Save(self):
		DB.save(self.database);
		return self;

	def Empty(self):
		return len(self.database) == 0;

	def LastIndex(self):
		return DB.lastIndex(db=self.database);

	def LastItem(self):
		return self.lastItem(db=self.database);

	def Find(self, key, value):
		return DB.find(key, value, db=self.database)
