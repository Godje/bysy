import sys;
import json;

class DB:
	@staticmethod
	def load():
		db = [];
		dbfilename = "db.json";
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
