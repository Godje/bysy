## Delete entry
def deleteentry():
	if(len(db) == 0):
		print "Database is empty";
		return;

	if( argLength < 3 ):
		print "Not enough arguments provided";
		return;
	else:
		item_index = find(db, 'i', args[2]);
		if(item_index != None):
			del db[item_index];
			save();
		else:
			print "No item with such id";
			return;
