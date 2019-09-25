from DB import DB;

## Delete entry
def deleteentry(args):
	db = DB().Load();

	if( db.Empty() ):
		print "Database is empty";
		return;

	if( len(args) != 1 ):
		print "Not enough arguments provided";
		return;

	else:
		item_index = db.Find('i', args[0]);
		if(item_index != None):
			del db.database[item_index];
			db.Save();
		else:
			print "No item with such id";
			return;
