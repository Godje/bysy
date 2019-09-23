from DB import DB;

## Delete entry
def deleteentry(args):
	db = DB.load();

	if(len(db) == 0):
		print "Database is empty";
		return;

	if( len(args) != 1 ):
		print "Not enough arguments provided";
		return;
	else:
		item_index = find(db, 'i', args[0]);
		if(item_index != None):
			del db[item_index];
			DB.save(db);
		else:
			print "No item with such id";
			return;

def find(lst, key, value):
	for entry in lst:
		if entry[key] == int(value):
			return lst.index(entry);
	return None;
